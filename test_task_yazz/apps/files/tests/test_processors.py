import pytest
from PIL import Image

from files.processors import EXIFOrientation


@pytest.fixture
def exif_data_with_orientation():
    """
    An EXIF metadata with the only parameter 'Orientation'.

    The value of the parameter is 6, that corresponds to a camera rotation by 270 degrees counterclockwise.
    """

    return (
        b'Exif\x00\x00MM\x00*\x00\x00\x00\x08\x00\x01\x01\x12\x00\x03\x00\x00\x00\x01\x00\x06\x00\x00\x00\x00\x00\x00'
    )


@pytest.fixture
def image_with_exif_orientation(temp_image, exif_data_with_orientation):
    image = Image.new('RGB', (80, 20))
    image.save(temp_image, exif=exif_data_with_orientation)
    temp_image.seek(0)

    return Image.open(temp_image)


class TestEXIFOrientation:

    def test_process(self, image_with_exif_orientation):
        processor = EXIFOrientation()

        result_image = processor.process(image_with_exif_orientation)
        assert result_image.width == 20  # should equals to initial image height from fixture
        assert result_image.height == 80  # should equals to initial image width from fixture
