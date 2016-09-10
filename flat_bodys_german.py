import turtle
import math

print("\n\n****************************************************************************\n\n")
print("\n****************************************************************************\n")
print("\n\nWenn ein Mass unbekannt, dann bitte null schreiben!\n")
print("Es muessen zwei Masse bekannt sein, um die Berechnung durchzufuehren!\n\n")
print("\n****************************************************************************\n")
while 1:
    t = str(input("Type des Vielecks r=Rechteck, p=Parallelogramm, dr=Dreieck, de=Deltoid, t=Trapez e=Exit : "))
    if t in ['e']:
        break
    elif t in ['r']:
        print("\n\n****************************************************************************\n\n")
        ar = float(input("Laenge der Seite a [mm] : "))
        br = float(input("Laenge der Seite b [mm] : "))
        Ar = float(input("Flaeche [mm**2] : "))
        #U = (a + b) * 2
        print("\n\n****************************************************************************\n\n")
        #print "Seite a = ", a, "[mm]"
        #print "Seite b = ", b, "[mm]"
        if Ar == 0:
            Br = ar * br
            print("Ergebnis: Flaeche des Rechtecks = %.1f" % Br, "[mm**2]")
            print("\n\n****************************************************************************\n\n")
        elif ar == 0:
            cr = Ar / br
            print("Ergebnis: Laenge der Seite a = %.5f" % cr, "[mm]")
            print("\n\n****************************************************************************\n\n")
            ar = cr
        elif br == 0:
            dr = Ar / ar
            print("Ergebnis: Laenge der Seite b = %.5f" % dr, "[mm]")
            print("\n\n****************************************************************************\n\n")
            br = dr
        else:
            print(":-(")
            print("\n\n****************************************************************************\n\n")
        window = turtle.Screen()
        turtle.hideturtle()
        turtle.forward(ar)
        turtle.left(90)
        turtle.forward(br)
        turtle.left(90)
        turtle.forward(ar)
        turtle.left(90)
        turtle.forward(br)
        turtle.left(90)
        window.exitonclick()
    elif t in ['p']:
        print("\n\n****************************************************************************\n\n")
        ap = float(input("Laenge der Seite a [mm] : "))
        hap = float(input("Laenge der Hoehe ha [mm] : "))
        Ap = float(input("Flaeche [mm**2] : "))
        alp = float(input("Groese des Winkel Alpha [grad] : "))
        #U = (a + b) * 2
        print("\n\n****************************************************************************\n\n")
        #print "Seite a = ", a, "[mm]"
        #print "Seite b = ", b, "[mm]"
        if Ap == 0:
            Bp = ap * hap
            print("Ergebnis: Flaeche des Parallelogramms = %.1f" % Bp, "[mm**2]")
            print("\n\n****************************************************************************\n\n")
        elif ap == 0:
            cp = Ap / hap
            print("Ergebnis: Laenge der Seite a = %.5f" % cp, "[mm]")
            print("\n\n****************************************************************************\n\n")
            ap = cp
        elif hap == 0:
            dp = Ap / ap
            print("Ergebnis: Laenge der Hoehe ha = %.5f" % dp, "[mm]")
            print("\n\n****************************************************************************\n\n")
            hap = dp
        else:
            print(":-(")
            print("\n\n****************************************************************************\n\n")
        window = turtle.Screen()
        turtle.hideturtle()
        turtle.forward(ap)
        turtle.left(180 - alp)
        turtle.forward(hap / math.sin(alp))
        turtle.left(alp)
        turtle.forward(ap)
        turtle.left(180 - alp)
        turtle.forward(hap / math.sin(alp))
        turtle.left(alp)
        window.exitonclick()
    elif t in ['dr']:
        print("\n\n****************************************************************************\n\n")
        cd = float(input("Laenge der Seite c [mm] : "))
        hcd = float(input("Laenge der Hoehe hc [mm] : "))
        Ad = float(input("Flaeche [mm**2] : "))
        ald = float(input("Groese des Winkel Alpha [grad] : "))
        #U = (a + b) * 2
        print("\n\n****************************************************************************\n\n")
        #print "Seite a = ", a, "[mm]"
        #print "Seite b = ", b, "[mm]"
        if Ad == 0:
            Bd = cd * hcd / 2
            print("Ergebnis: Flaeche des Dreiecks = %.1f" % Bd, "[mm**2]")
            print("\n\n****************************************************************************\n\n")
        elif cd == 0:
            Cd = Ad / hcd * 2
            print("Ergebnis: Laenge der Seite c = %.5f" % Cd, "[mm]")
            print("\n\n****************************************************************************\n\n")
            cd = Cd
        elif hcd == 0:
            dd = Ad / cd * 2
            print("Ergebnis: Laenge der Hoehe hc = %.5f" % dd, "[mm]")
            print("\n\n****************************************************************************\n\n")
            hcd = dd
        else:
            print(":-(")
            print("\n\n****************************************************************************\n\n")
        aldx = math.radians(ald)
        window = turtle.Screen()
        turtle.radians()
        turtle.ht()
        turtle.pd()
        turtle.goto(- cd / 2, 0)
        turtle.left(aldx)
        turtle.forward(hcd / math.sin(aldx))
        turtle.goto(cd / 2, 0)
        turtle.home()
    elif t in ['de']:
        print("\n\n****************************************************************************\n\n")
        ede = float(input("Laenge der Diagonale e [mm] : "))
        fde = float(input("Laenge der Diagonale f [mm] : "))
        Ade = float(input("Flaeche [mm**2] : "))
        alde = float(input("Groese des Winkel Alpha [grad] : "))
        #U = (a + b) * 2
        print("\n\n****************************************************************************\n\n")
        #print "Seite a = ", a, "[mm]"
        #print "Seite b = ", b, "[mm]"
        if Ade == 0:
            Bde = ede * fde / 2
            print("Ergebnis: Flaeche des Deltoids = %.1f" % Bde, "[mm**2]")
            print("\n\n****************************************************************************\n\n")
        elif ede == 0:
                Cde = Ade / fde * 2
                print("Ergebnis: Laenge der Diagonale e = %.5f" % Cde, "[mm]")
                print("\n\n****************************************************************************\n\n")
                ede = Cde
        elif fde == 0:
            dde = Ade / ede * 2
            print("Ergebnis: Laenge der Diagonale f = %.5f" % dde, "[mm]")
            print("\n\n****************************************************************************\n\n")
            fde = dde
        else:
            print(":-(")
            print("\n\n****************************************************************************\n\n")
        exde = fde / 2 / math.tan(alde / 2)
        window = turtle.Screen()
        turtle.ht()
        turtle.pd()
        turtle.goto(exde, -fde / 2)
        turtle.goto(ede, 0)
        turtle.goto(exde, fde / 2)
        turtle.home()
        window.exitonclick()
    elif t in ['t']:
        print("\n\n****************************************************************************\n\n")
        at = float(input("Laenge der Seite a [mm] : "))
        ct = float(input("Laenge der Seite c  [mm] : "))
        ht = float(input("Laenge der Hoehe h [mm] : "))
        At = float(input("Flaeche [mm**2] : "))
        #U = (a + b) * 2
        print("\n\n****************************************************************************\n\n")
        #print "Seite a = ", a, "[mm]"
        #print "Seite b = ", b, "[mm]"
        if At == 0:
            Bt = (at + ct) * ht / 2
            print("Ergebnis: Flaeche des Trapez = %.1f" % Bt, "[mm**2]")
            print("\n\n****************************************************************************\n\n")
        elif at == 0:
            Ct = 2 * At / ht - ct
            print("Ergebnis: Laenge der Seite a = %.5f" % Ct, "[mm]")
            print("\n\n****************************************************************************\n\n")
            at = Ct
        elif ct == 0:
            Dt = 2 * At / ht - at
            print("Ergebnis: Laenge der Seite c = %.5f" % Dt, "[mm]")
            print("\n\n****************************************************************************\n\n")
            ct = Dt
        elif ht == 0:
            dt = At / (at + ct) * 2
            print("Ergebnis: Laenge der Hoehe h = %.5f" % dt, "[mm]")
            print("\n\n****************************************************************************\n\n")
            ht = dt
        else:
            print(":-(")
            print("\n\n****************************************************************************\n\n")
        window = turtle.Screen()
        turtle.ht()
        turtle.pd()
        turtle.goto(-at / 2, 0)
        turtle.goto(-ct / 2, ht)
        turtle.goto(ct / 2, ht)
        turtle.goto(at / 2, 0)
        turtle.home()
        window.exitonclick()
    else:
        print("\n\n:-(\n\n")