from typing import List, Optional

from iamheadless_publisher_site.pydantic_models import BaseItemContentsPydanticModel, BaseItemDataPydanticModel, BaseItemPydanticModel

from .conf import settings


class ImageContentPydanticModel(BaseItemContentsPydanticModel):
    file_name: str
    language: str
    summary: Optional[str]
    title: str


class ImageDataPydanticModel(BaseItemDataPydanticModel):
    contents: List[ImageContentPydanticModel]


class ImagePydanticModel(BaseItemPydanticModel):
    _content_model = ImageContentPydanticModel
    _data_model = ImageDataPydanticModel
    _display_name_plural = 'images'
    _display_name_singular = 'image'
    _item_type = 'image'

    data: ImageDataPydanticModel
