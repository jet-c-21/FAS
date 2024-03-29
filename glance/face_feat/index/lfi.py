# coding: utf-8
import cv2
from glance.jf_ult.geom_tool import GeomTool
import numpy as np
from glance.jf_ult.lmk_helper import LMKHelper


class LFI:
    def __init__(self, landmarks: dict, img=None, calc_mode=None):
        # self.landmarks = landmarks
        self.image = img
        self.landmarks = landmarks
        self.calc_mode = calc_mode
        self.face_scale = LMKHelper.get_face_scale(self.landmarks)

        # calculate
        self.face_coords = self.get_face_coords()
        self.face_area = GeomTool.get_polygon_area(self.face_coords)
        self.face_perimeter = GeomTool.get_polygon_len(self.face_coords)

        self.val = self.face_perimeter / self.face_area
        self.val_2 = (self.face_perimeter * (self.face_scale['hrz'] + self.face_scale['vrt']) * 2) / (
                self.face_area * self.face_scale['hrz'] * self.face_scale['vrt'])

        # display
        self.red = (0, 0, 255)
        self.green = (0, 255, 0)
        self.thick = 2

    def get_face_coords(self):
        coords = []
        if self.calc_mode == 'p':
            lm_ids = ['1', '4', '9', '14', '17']
            for lm_id in lm_ids:
                coords.append(self.landmarks[lm_id])
        else:
            for i in range(17):
                lm_id = str(i + 1)
                coords.append(self.landmarks[lm_id])

        return coords

    def show(self, dest_path=None):
        temp = self.image.copy()
        wf_pts = np.array(self.face_coords, np.int32)
        wf_pts = wf_pts.reshape((-1, 1, 2))
        # cv2.fillPoly(temp, [wf_pts], self.red)
        cv2.polylines(temp, [wf_pts], True, self.red, 6)
        cv2.polylines(temp, [wf_pts], True, self.green, 2)

        if dest_path:
            cv2.imwrite(dest_path, temp)
        else:
            cv2.imshow('{}'.format(__name__), temp)
            cv2.waitKey(0)

