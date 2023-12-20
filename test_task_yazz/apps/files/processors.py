from PIL import Image, ExifTags


class EXIFOrientation:
    """
    Rotates/flips an image to correspond a value of 'Orientation' parameter in EXIF metadata (if present).

    Is used to keep original orientation of the image (As the EXIF metadata is lost after saving processed image).
    """

    orientation_rotations = {  # angles are in degrees counted clockwise
        1: None,
        8: Image.ROTATE_90,
        3: Image.ROTATE_180,
        6: Image.ROTATE_270,
    }
    mirrored_orientations = {
        2: 1,
        7: 8,
        4: 3,
        5: 6,
    }

    def process(self, img):
        exif_orientation = self._get_exif_orientation(img)

        if exif_orientation in self.mirrored_orientations:
            exif_orientation = self.mirrored_orientations[exif_orientation]
            is_mirrored = True
        else:
            is_mirrored = False

        rotation_method = self.orientation_rotations.get(exif_orientation)
        if rotation_method:
            img = img.transpose(method=rotation_method)
        if is_mirrored:
            img = img.transpose(method=Image.FLIP_LEFT_RIGHT)
        return img

    @staticmethod
    def _get_exif_orientation(img):
        exif_data = {
            ExifTags.TAGS[key]: value
            for key, value in img.getexif().items()
            if key in ExifTags.TAGS
        }

        return exif_data.get("Orientation")
