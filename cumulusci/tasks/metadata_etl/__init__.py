from cumulusci.tasks.metadata_etl.base import (
    BaseMetadataETLTask,
    BaseMetadataSynthesisTask,
    BaseMetadataTransformTask,
    MetadataSingleEntityTransformTask,
    get_new_tag_index,
    MD,
)
from cumulusci.tasks.metadata_etl.layouts import AddRelatedLists
from cumulusci.tasks.metadata_etl.permissions import AddPermissionSetPermissions
from cumulusci.tasks.metadata_etl.value_sets import AddValueSetEntries
from cumulusci.tasks.metadata_etl.sharing import SetOrgWideDefaults

flake8 = (
    BaseMetadataETLTask,
    BaseMetadataSynthesisTask,
    BaseMetadataTransformTask,
    MetadataSingleEntityTransformTask,
    AddRelatedLists,
    AddPermissionSetPermissions,
    AddValueSetEntries,
    SetOrgWideDefaults,
    get_new_tag_index,
    MD,
)
