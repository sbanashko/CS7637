from RavensFigure import RavensFigure
from RavensObject import RavensObject
from RavensProblem import RavensProblem

import os.path
from PIL import Image, ImageFilter, ImageDraw
import numpy as np

score_boundary = 800000


def Image_Score(image_A, image_B):
    widthA, heightA = image_A.size
    pxA = image_A.load()
    pxB = image_B.load()
    score = 0
    for i in range(widthA):  # for every pixel:
        for j in range(heightA):
            a = np.array(pxA[i, j])
            b = np.array(pxB[i, j])
            score = score + np.linalg.norm(a - b)
    return score


def Color_Black_white(imageInput):
    image_copy = imageInput.copy()
    width, height = image_copy.size
    px = image_copy.load()
    for i in range(width):  # for every pixel:
        for j in range(height):
            # print("px[i,j]:",px[i,j])
            if px[i, j] == (255, 255, 255, 255):
                px[i, j] = (255, 255, 255, 255)
            else:  # change to black
                px[i, j] = (0, 0, 0, 255)
    return image_copy


def fill_color(imageInput, color):
    # pkg_dir = os.path.dirname(__file__)
    image_copy = imageInput.copy()
    width, height = image_copy.size
    center = (int(0.5 * width), int(0.5 * height))
    # print("center:",center)
    ImageDraw.floodfill(image_copy, xy=center, border=None, value=color, thresh=0)
    imageOutput = Color_Black_white(image_copy)

    return imageOutput


imA = Image.open(
    "E:\Peng Chen\GT_OMCS_Application\Knowledge Based AI\Project\Project1\KBAI-package-python-master\Project-Code-Python\Problems\Challenge Problems B\Challenge Problem B-09/A.png")
imB = Image.open(
    "E:\Peng Chen\GT_OMCS_Application\Knowledge Based AI\Project\Project1\KBAI-package-python-master\Project-Code-Python\Problems\Challenge Problems B\Challenge Problem B-09/B.png")
imC = Image.open(
    "E:\Peng Chen\GT_OMCS_Application\Knowledge Based AI\Project\Project1\KBAI-package-python-master\Project-Code-Python\Problems\Challenge Problems B\Challenge Problem B-09/C.png")
im1 = Image.open(
    "E:\Peng Chen\GT_OMCS_Application\Knowledge Based AI\Project\Project1\KBAI-package-python-master\Project-Code-Python\Problems\Challenge Problems B\Challenge Problem B-09/1.png")
im2 = Image.open(
    "E:\Peng Chen\GT_OMCS_Application\Knowledge Based AI\Project\Project1\KBAI-package-python-master\Project-Code-Python\Problems\Challenge Problems B\Challenge Problem B-09/2.png")
im3 = Image.open(
    "E:\Peng Chen\GT_OMCS_Application\Knowledge Based AI\Project\Project1\KBAI-package-python-master\Project-Code-Python\Problems\Challenge Problems B\Challenge Problem B-09/3.png")
im4 = Image.open(
    "E:\Peng Chen\GT_OMCS_Application\Knowledge Based AI\Project\Project1\KBAI-package-python-master\Project-Code-Python\Problems\Challenge Problems B\Challenge Problem B-09/4.png")
im5 = Image.open(
    "E:\Peng Chen\GT_OMCS_Application\Knowledge Based AI\Project\Project1\KBAI-package-python-master\Project-Code-Python\Problems\Challenge Problems B\Challenge Problem B-09/5.png")
im6 = Image.open(
    "E:\Peng Chen\GT_OMCS_Application\Knowledge Based AI\Project\Project1\KBAI-package-python-master\Project-Code-Python\Problems\Challenge Problems B\Challenge Problem B-09/6.png")


# Basic transformation for A to B, or A to C
# 1.Identical(do nothing),
# 2.horizontal reflection or vertical reflection
# 2.1 horizontal reflection
# imA_Vertical_reflect.show()
# 2.1 horizontal reflection
# imA_Horizontal_reflect.show()
# 3.rotate 90 degrees, 180 degrees, 270 degrees
# imA_rotate90.show()
# imA.show()
# 4.Solid to stripe/stripe to solid
# 5.solid to hollow/hollow to solid
# 5.1 solid to hollow
# imA_hollow = imA.filter(ImageFilter.CONTOUR)
# 5.2 hollow to solid
# imA_hollow = imA.filter(ImageFilter.CONTOUR)
def image_transformation(imageInput, transformNum):
    image_output = imageInput.copy()
    if transformNum == 1:
        image_output = imageInput.copy()
    elif transformNum == 2:
        # Image_input FLIP LEFT_RIGHT to Image_output
        image_output = imageInput.transpose(Image.FLIP_LEFT_RIGHT)
    elif transformNum == 3:
        # Image_input FLIP_TOP_BOTTOM  to Image_output
        image_output = imA.transpose(Image.FLIP_TOP_BOTTOM)
    elif transformNum == 4:
        # Image_input Rotates 90 degree to Image_output
        image_output = imA.transpose(Image.ROTATE_90)
    elif transformNum == 5:
        # Image_input Rotates 180 degree to Image_output
        image_output = imA.transpose(Image.ROTATE_180)
    elif transformNum == 6:
        # Image_input Rotates 270 degree to Image_output
        image_output = imA.transpose(Image.ROTATE_270)
    elif transformNum == 7:
        # Image_input becomes solid Black to Image_output
        image_output = fill_color(imageInput=imA, color=(0, 0, 0, 255))
    elif transformNum == 8:
        # Image_input becomes hollow
        image_output = fill_color(imageInput=imA, color=(255, 255, 255, 255))

    return image_output


def Image_relationship_identify(imageA, imageB):
    if Image_Score(image_A=image_transformation(imageInput=imageA, transformNum=1), image_B=imageB) < score_boundary:
        print("Image A is identical to Image B")
        return 1
    elif Image_Score(image_A=image_transformation(imageInput=imageA, transformNum=2), image_B=imageB) < score_boundary:
        print("Image A FLIP LEFT_RIGHT to Image B")
        return 2
    elif Image_Score(image_A=image_transformation(imageInput=imageA, transformNum=3), image_B=imageB) < score_boundary:
        print("Image A FLIP_TOP_BOTTOM to Image B")
        return 3
    elif Image_Score(image_A=image_transformation(imageInput=imageA, transformNum=4), image_B=imageB) < score_boundary:
        print("Image A Rotates 90 degree to Image B")
        return 4
    elif Image_Score(image_A=image_transformation(imageInput=imageA, transformNum=5), image_B=imageB) < score_boundary:
        print("Image A Rotates 180 degree to Image B")
        return 5
    elif Image_Score(image_A=image_transformation(imageInput=imageA, transformNum=6), image_B=imageB) < score_boundary:
        print("Image A Rotates 270 degree to Image B")
        return 6
    elif Image_Score(image_A=image_transformation(imageInput=imageA, transformNum=7), image_B=imageB) < score_boundary:
        print("Image A becomes solid Black then identical to Image B")
        return 7
    elif Image_Score(image_A=image_transformation(imageInput=imageA, transformNum=8), image_B=imageB) < score_boundary:
        print("Image A becomes hollow then identical to Image B")
        return 8

A_B_Relationship_num = Image_relationship_identify(imageA=imA, imageB=imB)
Potential_answer_D_AB = image_transformation(imageInput=imC, transformNum=A_B_Relationship_num)
A_C_Relationship_num = Image_relationship_identify(imageA=imA, imageB=imC)
Potential_answer_D_AC = image_transformation(imageInput=imC, transformNum=A_C_Relationship_num)


def Look_for_answer(imageInput, transfom_num):
    answer_score_list = []
    image_dic = {1:im1,2:im2,3:im3,4:im4,5:im5,6:im6}
    for i in range(1, 7):
        print(i)
        answer_N = image_dic.get(i)
        answer_score_list.append(Image_Score(image_A=imageInput, image_B=answer_N))

    # return the answer with the minimum score
    return answer_score_list.index(min(answer_score_list)), min(answer_score_list)

answer1, score1 = Look_for_answer(imageInput = Potential_answer_D_AB, transfom_num = A_B_Relationship_num)
#answer2, score2 = Look_for_answer(imageInput = Potential_answer_D_AC, transfom_num = A_C_Relationship_num)

print("answer1, score1",answer1, score1)
#print("answer2, score2",answer2, score2)
