# coding: utf-8
import cv2
from glance.jf_ult.geom_tool import GeomTool
from glance.jf_ult.lmk_helper import LMKHelper


class CJWR:
    def __init__(self, landmarks: dict, img=None):
        self.image = img
        self.landmarks = landmarks
        self.face_scale = LMKHelper.get_face_scale(self.landmarks)

        # calculate
        # cheek part
        self.left_cheek = self.landmarks['17']
        self.right_cheek = self.landmarks['1']
        self.cheek_width = GeomTool.get_pt_dist(self.left_cheek, self.right_cheek)

        # jaw part
        self.right_jaw = self.landmarks['5']
        self.left_jaw = self.landmarks['13']
        self.jaw_width = GeomTool.get_pt_dist(self.right_jaw, self.left_jaw)

        self.val = self.jaw_width / self.cheek_width
        self.val_2 = (self.jaw_width * self.cheek_width) / (self.face_scale['hrz'] ** 2)

        # display
        self.red = (0, 0, 255)
        self.green = (0, 255, 0)
        self.thick = 2

    def show(self, dest_path=None):
        temp = self.image.copy()
        cv2.line(temp, self.right_cheek, self.left_cheek, self.red, self.thick)
        cv2.line(temp, self.right_jaw, self.left_jaw, self.green, self.thick)

        if dest_path:
            cv2.imwrite(dest_path, temp)
            return temp
        else:
            cv2.imshow('{}'.format(__name__), temp)
            cv2.waitKey(0)
