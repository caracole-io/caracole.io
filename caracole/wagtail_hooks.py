import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail import hooks
from wagtail.admin.rich_text.converters.html_to_contentstate import BlockElementHandler


@hooks.register("register_rich_text_features")
def register_blockquote_feature(features):
    """https://docs.wagtail.io/en/v2.3/advanced_topics/customisation/
        extending_draftail.html#creating-new-blocks
    Registering the `blockquote` feature, which uses the `blockquote` Draft.js block
    type, and is stored as HTML with a `<blockquote>` tag.
    """
    feature_name = "blockquote"
    type_ = "blockquote"
    tag = "blockquote"

    control = {
        "type": type_,
        "label": "❝",
        "description": "Blockquote",
        # Optionally, we can tell Draftail what element to use
        # when displaying those blocks in the editor.
        "element": "blockquote",
    }

    features.register_editor_plugin(
        "draftail",
        feature_name,
        draftail_features.BlockFeature(control),
    )

    features.register_converter_rule(
        "contentstate",
        feature_name,
        {
            "from_database_format": {tag: BlockElementHandler(type_)},
            "to_database_format": {"block_map": {type_: tag}},
        },
    )
    features.default_features.append("blockquote")
