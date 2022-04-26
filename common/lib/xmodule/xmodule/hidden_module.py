"""
The Hidden XBlock.
"""

from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xmodule.raw_module import RawMixin
from xmodule.xml_module import XmlMixin
from xmodule.x_module import (
    XModuleDescriptorToXBlockMixin,
    XModuleMixin,
    XModuleToXBlockMixin,
)


@XBlock.needs("i18n")
class HiddenDescriptor(
    RawMixin,
    XmlMixin,
    XModuleDescriptorToXBlockMixin,
    XModuleToXBlockMixin,
    XModuleMixin,
):
    """
    XBlock class loaded by the runtime when another XBlock type has been disabled
    or an unknown XBlock type is included in a course import.

    The class name includes 'Descriptor' because this used to be an XModule and the class path is specified in the
    modulestore config in a number of places.
    """
    HIDDEN = True
    has_author_view = True

    resources_dir = None

    def author_view(self, _context):
        """
        Return the author view.
        """
        fragment = Fragment()
        _ = self.runtime.service(self, "i18n").ugettext
        content = _(
            'ERROR: "{block_type}" is an unknown component type. This component will be hidden in LMS.'
        ).format(block_type=self.scope_ids.block_type)
        fragment.add_content(content)
        return fragment

    def studio_view(self, _context):
        """
        Return the studio view.
        """
        # User should not be able to edit unknown types.
        fragment = Fragment()
        return fragment

    def student_view(self, _context):
        """
        Return the student view.
        """
        fragment = Fragment()
        return fragment
