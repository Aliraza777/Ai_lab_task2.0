import csv
from numpy.lib.twodim_base import diag
import cv2
import numpy


img = cv2.imread("./Apple02.jpg" ,cv2.IMREAD_GRAYSCALE)


def whatItDoes(img):

    a , b = img.shape
    elements1 = numpy.empty(a)
    k = 0
    for j in range(100):

        if(img[j][j]!='nan'):

            elements1[k] = img[j][j]
        else:
            elements1[k]=0
            k=k+1
    return elements1


#~~~~~~sum and Average of Diagonal One
def Diagalone(img):
    sum = 0
    for j in range(100):
        if(img[j][j]!='nan'):
            sum += img[j][j]

        avgofDiagOne = sum / 100
        return sum , avgofDiagOne

#~~~~~~sum and Average of Diagonal Two
def DiagalTwo(img):
    sum = 0
    for j in range(100):

        if(img[j][99-j]!='nan'):
            sum += img[j][99-j]

        avgofDiagTwo = sum / 100
        return sum , avgofDiagTwo


#~~~~~~sum and Average of first Thirty columns
def avgFirstThirtyCols(img):
    sum = 0
    for i in range(100):
        for j in range(30):
            if(img[i][j]!='nan'):
                sum += img[i][j]

        return sum , sum/3000

#~~~~~~sum and Average of last Thirty columns
def avgLastThirtyCols(img):
    sum = 0
    for i in range(100):
        for j in range(30):
            if(img[i][j+70]!='nan'):
                sum += img[i][j+70]

        return sum , sum/3000

#~~~~~~sum and Average of first Thirty Rows
def avgFirstThirtyRows(img):
    sum = 0
    for i in range(30):
        for j in range(100):
            if(img[i][j]!='nan'):
                sum += img[i][j]

        return sum , sum/3000

#~~~~~~sum and Average of last Thirty columns
def avgLastThirtyRows(img):
    sum = 0
    for i in range(30):
        for j in range(100):
            if(img[i][j]!='nan'):
                sum += img[i+70][j]

        return sum , sum/3000


if __name__ == '__main__':
    
    # cv2.imshow('Apple' , img)
    sumdiag1 , Avgdiag1 = Diagalone(img)
    sumdiag2 , Avgdiag2 = DiagalTwo(img)
    sumfirst30cols , avgfirst30cols = avgFirstThirtyCols(img)
    sumlast30cols , avglast30cols = avgLastThirtyCols(img)
    sumfirst30rows , avgfirst30rows = avgFirstThirtyRows(img)
    sumlast30rows , avglast30rows = avgLastThirtyRows(img)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
#------------------
    sum1 = "SumDiagOne()"
    sum2 = "SumDiagTwo()"
    avg1 = "AvgDiagOne()"
    avg2 = "AvgDiagTwo()"
    avgf30cols = "AvgFirstThirtyCols()"
    avgl30cols = "AvgLastThirtyCols()"
    avgf30rows = "AvgFirstThirtyRows()"
    avgl30rows = "AvgLastThirtyRows()"

    with open('Features.csv' , mode='w') as features:
        features_writer = csv.writer(features , delimiter = ',')

        features_writer.writerow(['Features axtracted from picture'])
        features_writer.writerow([sum1 , avg1 , sum2 , avg2 , avgf30cols , avgl30cols , avgf30rows , avgl30rows ])
        features_writer.writerow([sumdiag1 , Avgdiag1 , sumdiag2 , Avgdiag2 , avgfirst30cols ,avglast30cols , avgfirst30rows , avglast30rows ])   
           
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
