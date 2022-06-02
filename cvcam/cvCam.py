import cv2
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(prog="CVCam Tool for SoC")
    parser.add_argument("-camera",default=1,type=int,help="Set Camera Index")
    parser.add_argument('-version',action='version',version='%(prog)s 0.0.1')
    args=parser.parse_args()   
    cap2 = cv2.VideoCapture(args.camera)
    # cap2.set(cv2.CAP_PROP_AUTO_WB,0)
    # cap2.set(cv2.CAP_PROP_WB_TEMPERATURE,6000)
    # cap2.set(cv2.CAP_PROP_AUTO_EXPOSURE,0)
    while(cv2.waitKey(30)!=27):
        ret2,frame2 = cap2.read()
        if ret2:
            print("[INFO] Frame Shape : ",frame2.shape)
            cv2.imwrite('test_frame_soc.jpg',frame2)
            keyword=input("Use : q (quit) or c (continue) :")
            if (keyword == 'q'):
                sys.exit()

    cap2.release()
    cv2.destroyAllWindows()