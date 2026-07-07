from v0.2.models.institution import Institution
from v0.2.models.capability import Capability


class ModelConverter:
    """Convert loaded YAML data into GPS domain objects."""

    def convert(self, data):
        institution_data = data.get("institution", {})
        institution = Institution(
            institution_data.get("id"),
            institution_data.get("name"),
        )

        for capability_data in data.get("capabilities", []):
            capability = Capability(
                capability_data.get("id"),
                capability_data.get("name"),
                capability_data.get("maturity", 0),
            )
            institution.add_capability(capability)

        return institution
