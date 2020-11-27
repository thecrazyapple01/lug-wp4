import math
from fourpointfour import holes
from main import solutions_43,youngsm


def ThermalCheck(geometry,holes,t):
    Eb = 
    youngsbackplate = youngsm[geometry[3]] 
    

    Dlst = []
    Frlst = []
    for i in holes:
        Dsublst = []
        Dfi = 2 * holes[holes.index(i)][0]
        Dfo = 1.20 * 2 * holes[holes.index(i)][0]
        Dsublst.append(Dfi)
        Dsublst.append(Dfo)
        Dlst.append(Dsublst)
        della = (4 * t2) / (youngsbackplate *math.pi * (Dfo**2 - Dfi**2))
        dellb = (1/Eb)*(((0.4 * 4)/(math.pi * Dfo))+((0.4 * 4)/(math.pi * Dfi))+((0.4 * 4)/(math.pi * Dfo)))
        Fratio = della / (della + dellb)
        Frlst.append(Fratio)

    MaxFratio = max(Frlst)
    absorbtivity = 0.525
    emissivity = 0.09

    alphac = #thermal coefficient hinge
    alphab = #thermal coefficient bolt
    

    C =    #backplate width
    B =    #backplate length
    y = 
    w = 
    D1 = 

    Aabs = t2 * c + y * w + 0.5 * math.pi *(w/2)**2 - math.pi * (D1/2)**2
    Aemit = 2* Aabs + 2* (B * t2 + 2*(t1*(y+((D1/2)+(w-D1)/2))) + B * C


    Tmax = (((1665*absorbtivity + 179 * emissivity)*Aabs)/((5.67e-8)*emissivity*Aemit))**(1/4)
    Tmin = ((179*Aabs)/((5.67e-8)*Aemit))**(1/4)


    DeltaTmax = Tmax - 288.15
    DeltaTmin = Tmin - 288.15

    Dfi = holes[0[0]]
    

    FdeltaTmax = (alphac - alphab) * DeltaTmax * Eb * (math.pi*(Dfi/2)**2) * (1-MaxFratio)
    FdeltaTmin = (alphac - alphab) * DeltaTmin * Eb * (math.pi*(Dfi/2)**2) * (1-MaxFratio)

    Asum = 0
    Axsum = 0
    Azsum = 0

    Fx = 1427.4 + FdeltaTmax
    Fz = 665.7 + FdeltaTmax

    Ax2sum = 0
    Az2sum = 0

    Finplanemylst = []
    sigma = material_bearing_strength

    for i in holes:
        Asum = Asum + (math.pi) * (holes[holes.index(i)][0])**2
        Axsum = Axsum + ((math.pi) * (holes[holes.index(i)][0])**2) * (holes[holes.index(i)][1])
        Azsum = Azsum + ((math.pi) * (holes[holes.index(i)][0])**2) * (holes[holes.index(i)][2])

        Finplanemysublst = []
        Ax = ((math.pi) * (holes[holes.index(i)][0])**2) * (holes[holes.index(i)][1] - xcg)
        Az = ((math.pi) * (holes[holes.index(i)][0])**2) * (holes[holes.index(i)][2] - zcg)
        Ax2sum = Ax2sum + ((math.pi) * (holes[holes.index(i)][0])**2) * ((holes[holes.index(i)][1] - xcg)**2)
        Az2sum = Az2sum + ((math.pi) * (holes[holes.index(i)][0])**2) * ((holes[holes.index(i)][2] - zcg)**2)
        Finplane_my_x = (M_cg_y * Az)/(Az2sum)
        Finplane_my_z = (M_cg_y * Ax)/(Ax2sum)
        Finplanemysublst.append(Finplane_my_x)
        Finplanemysublst.append(Finplane_my_z)
        Finplanemylst.append(Finplanemysublst)
    xcg = Axsum / Asum
    zcg = Azsum / Asum
    nf = len(holes)
    M_cg_y = Fz * xcg - Fx * zcg
    F_in_plane_x = Fx / nf
    F_in_plane_z = Fz / nf

    Pilst = []
    for i in Finplanemylst:
        Fnetx = F_in_plane_x + Finplanemylst[Finplanemylst.index(i)][1]
        Fnetz = F_in_plane_z + Finplanemylst[Finplanemylst.index(i)][2]
        Pi = math.sqrt((Fnetx**2) + (Fnetz**2))
        Pilst.append(Pi)
    
    sigmalist = []
    for i in Pilst:
        sigma = Pilst[Pilst.index(i)] / (2 * t * holes[Pilst.index(i)][0])
        sigmalist.append(sigma)
    
    MSlist = []
    for i in sigmalist:
        MS = (sigmalist[sigmalist.index(i)] / material_bearing_strength) - 1
        MSlist.append(MS)

    return min(MSlist)