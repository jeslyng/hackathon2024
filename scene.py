from manim import *

class Circ(Scene):
    def construct(self):
        n = 2
        p1 = [-4/n,-5/n,0]
        p2 = [-2/n,-5/n,0]
        p3 = [-2/n,-2/n,0]
        p4 = [-2/n,-1.5/n,0]
        p5 = [0,-1.5/n,0]
        a1 = Line(p1,p2).append_points(Line(p2,p3).points).append_points(Line(p3,p4).points).append_points(Line(p4,p5).points)

        p6 = [1/n,-1.5/n,0]
        p7 = [1/n,-2/n,0]
        p8 = [-7/n,-2/n,0]
        p9 = [-7/n,2/n,0]
        p10 = [-6/n,2/n,0]
        a2 = Line(p5,p6).append_points(Line(p6,p7).points).append_points(Line(p7,p8).points)
        a21 = Line(p8,p9).append_points(Line(p9,p10).points)

        p11 = [-4/n,2/n,0]
        a3 = Line(p10,p11)

        p12 = [-4/n,3/n,0]
        p13 = [7/n,2/n,0]
        a4 = Line(p11,p12).append_points(Line(p12,p13).points)

        p14 = [7/n,-2/n,0]
        p15 = [3/n,-2/n,0]
        p16 = [3/n,-1/n,0]
        a5 = Line(p13,p14).append_points(Line(p14,p15).points).append_points(Line(p15,p16).points)

        a6 = Line(p16,p15).append_points(Line(p15,p3).points).append_points(Line(p3,p4).points).append_points(Line(p4,p5).points)

        p17 = [-7/n,-5/n,0]
        a7 = Line(p5,p6).append_points(Line(p6,p7).points).append_points(Line(p7,p8).points).append_points(Line(p8,p17).points)
        
        a8 = Line(p17,p1)

        dot = Dot()

        self.add(a1)
        self.add(a2)
        self.add(a21)
        self.add(a3)
        self.add(a4)
        self.add(a5)
        self.add(a6)
        self.add(a7)
        self.add(a8)

        self.add(Dot(p1).set_color(DARK_BLUE).scale(2))
        self.add(Dot(p5).set_color(DARK_BLUE).scale(2))
        self.add(Dot(p10).set_color(DARK_BLUE).scale(2))
        self.add(Dot(p11).set_color(DARK_BLUE).scale(2))
        self.add(Dot(p13).set_color(DARK_BLUE).scale(2))
        self.add(Dot(p16).set_color(DARK_BLUE).scale(2))
        self.add(Dot(p17).set_color(DARK_BLUE).scale(2))

        self.play(MoveAlongPath(dot,a1), run_time=2)
        self.play(MoveAlongPath(dot,a2), run_time=1.5,rate_func=rate_functions.ease_in_sine)
        self.play(MoveAlongPath(dot,a21), run_time=1.5,rate_func=rate_functions.ease_out_sine)
        self.play(MoveAlongPath(dot,a3), run_time=2)
        self.play(MoveAlongPath(dot,a4), run_time=3)
        self.play(MoveAlongPath(dot,a5), run_time=3)
        self.play(MoveAlongPath(dot,a6), run_time=3)
        self.play(MoveAlongPath(dot,a7), run_time=3)
        self.play(MoveAlongPath(dot,a8), run_time=1.5)
        self.wait(2)

class Loop(Scene):
    def construct(self):
        n = 3
        pl1 = [-4/n,-5/n,0]
        pl2 = [-2/n,-5/n,0]
        pl3 = [-2/n,-1.5/n,0]
        pl4 = [0,-1.5/n,0]
        al1 = Line(pl1,pl2).append_points(Line(pl2,pl3).points).append_points(Line(pl3,pl4).points)

        pl5 = [1/n,-1.5/n,0]
        pl6 = [1/n,-2/n,0]
        pl7 = [7/n,-2/n,0]
        pl8 = [7/n,10/n,0]
        pl9 = [6/n,10/n,0]
        al2 = Line(pl4,pl5).append_points(Line(pl5,pl6).points).append_points(Line(pl6,pl7).points)
        al21 = Line(pl7,pl8).append_points(Line(pl8,pl9).points)

        pl10 = [6/n,11/n,0]
        pl11 = [5/n,11/n,0]
        al3 = Line(pl9,pl10).append_points(Line(pl10,pl11).points)

        pl12 = [2/n,11/n,0]
        al4 = Line(pl11,pl12)
        
        pl13 = [2/n,10/n,0]
        pl14 = [1/n,10/n,0]
        pl15 = [1/n,8/n,0]
        al5 = Line(pl12,pl13).append_points(Line(pl13,pl14).points).append_points(Line(pl14,pl15).points)

        pl16 = [-2/n,8/n,0]
        al6 = Line(pl15,pl16)

        pl17 = [-4/n,8/n,0]
        pl18 = [-4/n,9/n,0]
        al7 = Line(pl16,pl17).append_points(Line(pl17,pl18).points)
        
        pl19 = [-4/n,10/n,0]
        pl20 = [-7/n,10/n,0]
        pl21 = [-7/n,-5/n,0]
        al8 = Line(pl18,pl19).append_points(Line(pl19,pl20).points)
        al81 = Line(pl20,pl21)
        
        al9 = Line(pl21,pl1)

        dot = Dot()

        self.add(al1)
        self.add(al2)
        self.add(al21)
        self.add(al3)
        self.add(al4)
        self.add(al5)
        self.add(al6)
        self.add(al7)
        self.add(al8)
        self.add(al81)
        self.add(al9)

        self.add(Dot(pl1).set_color(DARK_BLUE).scale(2))
        self.add(Dot(pl4).set_color(DARK_BLUE).scale(2))
        self.add(Dot(pl9).set_color(DARK_BLUE).scale(2))
        self.add(Dot(pl11).set_color(DARK_BLUE).scale(2))
        self.add(Dot(pl12).set_color(DARK_BLUE).scale(2))
        self.add(Dot(pl15).set_color(DARK_BLUE).scale(2))
        self.add(Dot(pl16).set_color(DARK_BLUE).scale(2))
        self.add(Dot(pl18).set_color(DARK_BLUE).scale(2))
        self.add(Dot(pl21).set_color(DARK_BLUE).scale(2))

        self.play(MoveAlongPath(dot,al1), run_time=2)
        self.play(MoveAlongPath(dot,al2), run_time=1,rate_func=rate_functions.ease_in_sine)
        self.play(MoveAlongPath(dot,al21), run_time=1.5,rate_func=rate_functions.ease_out_sine)
        self.play(MoveAlongPath(dot,al3), run_time=0.75)
        self.play(MoveAlongPath(dot,al4), run_time=1)
        self.play(MoveAlongPath(dot,al5), run_time=1.5)
        self.play(MoveAlongPath(dot,al6), run_time=1)
        self.play(MoveAlongPath(dot,al7), run_time=1)
        self.play(MoveAlongPath(dot,al8), run_time=1,rate_func=rate_functions.ease_in_sine)
        self.play(MoveAlongPath(dot,al81), run_time=2,rate_func=rate_functions.ease_out_sine)
        self.play(MoveAlongPath(dot,al9), run_time=1)
        self.wait(2)

class Everything(Scene):
    
    def construct(self):
        #initializing Circ
        n = 2.5
        p1 = [-4/n,-5/n,0]
        p2 = [-2/n,-5/n,0]
        p3 = [-2/n,-2/n,0]
        p4 = [-2/n,-1.5/n,0]
        p5 = [0,-1.5/n,0]
        a1 = Line(p1,p2).append_points(Line(p2,p3).points).append_points(Line(p3,p4).points).append_points(Line(p4,p5).points)

        p6 = [1/n,-1.5/n,0]
        p7 = [1/n,-2/n,0]
        p8 = [-7/n,-2/n,0]
        p9 = [-7/n,2/n,0]
        p10 = [-6/n,2/n,0]
        a2 = Line(p5,p6).append_points(Line(p6,p7).points).append_points(Line(p7,p8).points)
        a21 = Line(p8,p9).append_points(Line(p9,p10).points)

        p11 = [-4/n,2/n,0]
        a3 = Line(p10,p11)

        p12 = [-4/n,3/n,0]
        p13 = [7/n,2/n,0]
        a4 = Line(p11,p12).append_points(Line(p12,p13).points)

        p14 = [7/n,-2/n,0]
        p15 = [3/n,-2/n,0]
        p16 = [3/n,-1/n,0]
        a5 = Line(p13,p14).append_points(Line(p14,p15).points).append_points(Line(p15,p16).points)

        a6 = Line(p16,p15).append_points(Line(p15,p3).points).append_points(Line(p3,p4).points).append_points(Line(p4,p5).points)

        p17 = [-7/n,-5/n,0]
        a7 = Line(p5,p6).append_points(Line(p6,p7).points).append_points(Line(p7,p8).points).append_points(Line(p8,p17).points)
        
        a8 = Line(p17,p1)

        

  

        dot1 = Dot(p1).set_color(DARK_BLUE).scale(2)
        dot2 = Dot(p5).set_color(DARK_BLUE).scale(2)
        dot3 = Dot(p10).set_color(DARK_BLUE).scale(2)
        dot4 = Dot(p11).set_color(DARK_BLUE).scale(2)
        dot5 = Dot(p13).set_color(DARK_BLUE).scale(2)
        dot6 = Dot(p16).set_color(DARK_BLUE).scale(2)
        dot7 = Dot(p17).set_color(DARK_BLUE).scale(2)

        CircGroupLines = VGroup(
            a1, a2, a21, a3, a4, a5, a6, a7, a8
        )
        CircGroupDots = VGroup(
            dot1, dot2, dot3, dot4, dot5, dot6, dot7
        )
        
        #initializing Loop
        pl1 = [-4/n,-5/n,0]
        pl2 = [-2/n,-5/n,0]
        pl3 = [-2/n,-1.5/n,0]
        pl4 = [0,-1.5/n,0]
        al1 = Line(pl1,pl2).append_points(Line(pl2,pl3).points).append_points(Line(pl3,pl4).points)

        pl5 = [1/n,-1.5/n,0]
        pl6 = [1/n,-2/n,0]
        pl7 = [7/n,-2/n,0]
        pl8 = [7/n,10/n,0]
        pl9 = [6/n,10/n,0]
        al2 = Line(pl4,pl5).append_points(Line(pl5,pl6).points).append_points(Line(pl6,pl7).points)
        al21 = Line(pl7,pl8).append_points(Line(pl8,pl9).points)

        pl10 = [6/n,11/n,0]
        pl11 = [5/n,11/n,0]
        al3 = Line(pl9,pl10).append_points(Line(pl10,pl11).points)

        pl12 = [2/n,11/n,0]
        al4 = Line(pl11,pl12)
        
        pl13 = [2/n,10/n,0]
        pl14 = [1/n,10/n,0]
        pl15 = [1/n,8/n,0]
        al5 = Line(pl12,pl13).append_points(Line(pl13,pl14).points).append_points(Line(pl14,pl15).points)

        pl16 = [-2/n,8/n,0]
        al6 = Line(pl15,pl16)

        pl17 = [-4/n,8/n,0]
        pl18 = [-4/n,9/n,0]
        al7 = Line(pl16,pl17).append_points(Line(pl17,pl18).points)
        
        pl19 = [-4/n,10/n,0]
        pl20 = [-7/n,10/n,0]
        pl21 = [-7/n,-5/n,0]
        al8 = Line(pl18,pl19).append_points(Line(pl19,pl20).points)
        al81 = Line(pl20,pl21)
        
        al9 = Line(pl21,pl1)

        bdot1=Dot(pl1).set_color(RED_C).scale(2)
        bdot2=Dot(pl4).set_color(RED_C).scale(2)
        bdot3=Dot(pl9).set_color(RED_C).scale(2)
        bdot4=Dot(pl11).set_color(RED_C).scale(2)
        bdot5=Dot(pl12).set_color(RED_C).scale(2)
        bdot6=Dot(pl15).set_color(RED_C).scale(2)
        bdot7=Dot(pl16).set_color(RED_C).scale(2)
        bdot8=Dot(pl18).set_color(RED_C).scale(2)
        bdot9=Dot(pl21).set_color(RED_C).scale(2)

        LoopGroupLines = VGroup(
            al1, al2, al21, al3, al4, al5, al6, al7, al8, al81, al9, 
        )
        LoopGroupDots = VGroup(
            bdot1, bdot2, bdot3, bdot4, bdot5, bdot6, bdot7, bdot8, bdot9
        )
        

        #Create Buildings

        DUC = Text("DUC", font_size=20)
        DUC.move_to([-0.5, -1.8, 0])
        South40 = Text("South 40", font_size=20)
        South40.move_to([-2.1,-3.15,0])
        Danforth = Text("Danforth Campus", font_size = 24)
        Danforth.move_to([0,-1.3,0])
        Danforth.set_opacity(0.6)
        Music = Text("560", font_size = 18)
        Music.move_to([-1.15,2.1,0])
        TheVillage = Text("The Village", font_size = 16)
        TheVillage.move_to([-2.2,-0.4,0])
        Lofts = Text("Lofts", font_size=20)
        Lofts.move_to([1.3,2.3,0])
        Lofts = Text("Lofts", font_size=20)
        Lofts.move_to([1.5,2.6,0])
        Loop = Text("Loop", font_size = 30)
        Loop.move_to([-0.6,2.7,0])
        Loop.set_opacity(0.6)


        building = VGroup(DUC, South40, Danforth, Music, TheVillage, Lofts, Loop)

        #create Dot
        dot = Dot(color=WHITE)

        #Group of Groups
        MegaGroup = VGroup(dot, CircGroupLines, CircGroupDots, LoopGroupLines, LoopGroupDots, building)

        #Create Scene
        
        self.add(LoopGroupLines, CircGroupLines, building)
        LoopGroupLines.set_color(color=[GRAY])
        self.add(LoopGroupDots)
        LoopGroupDots.set_opacity(0.6)
        self.add(CircGroupDots)
        self.add_foreground_mobject(dot)

        CircGroupLines.shift(1.5*DOWN)
        CircGroupDots.shift(1.5*DOWN)
        LoopGroupLines.shift(1.5*DOWN)
        LoopGroupDots.shift(1.5*DOWN)
        MegaGroup.scale(1.75)
        MegaGroup.shift(3*UP)
        dot.move_to(dot1.get_center())
        
        #names
        CircText = Text("Campus Circulator", font_size=48)
        CircText.to_corner(DR)
        LoopText = Text("Delmar Loop", font_size=48)
        LoopText.to_corner(DR)
        Example = Text("560 to The Village")
        Example.to_corner(DR)
        ExampleText = Text("Example Route:")
        ExampleText.to_corner(UL)
        self.play(FadeIn(CircText))

        #run full circ

        self.play(MoveAlongPath(dot,a1), run_time=2.2)
        self.play(MoveAlongPath(dot,a2), run_time=1.5,rate_func=rate_functions.ease_in_sine)
        self.play(MoveAlongPath(dot,a21), run_time=1.5,rate_func=rate_functions.ease_out_sine)
        self.play(MoveAlongPath(dot,a3), run_time=2)
        self.play(MoveAlongPath(dot,a4), run_time=3)
        self.play(MoveAlongPath(dot,a5), run_time=3)
        self.play(MoveAlongPath(dot,a6), run_time=3)
        self.play(MoveAlongPath(dot,a7), run_time=3)
        self.play(MoveAlongPath(dot,a8), run_time=1.5)

        #inbetween stuff
        self.play(MegaGroup.animate.scale(0.57))
        self.play(MegaGroup.animate.shift(3*DOWN))
        self.play(CircGroupDots.animate.set_opacity(0.6), run_time=0.25)
        self.play(CircGroupLines.animate.set_color(color=[GRAY]), run_time=0.25)
        self.play(LoopGroupDots.animate.set_opacity(1),run_time=0.25)
        self.play(LoopGroupLines.animate.set_color(color=[WHITE]), run_time=0.25)
        self.add(LoopGroupDots)
        self.play(Transform(CircText,LoopText))

        #run full loop
        self.play(MoveAlongPath(dot,al1), run_time=2)
        self.play(MoveAlongPath(dot,al2), run_time=1.5,rate_func=rate_functions.ease_in_sine)
        self.play(MoveAlongPath(dot,al21), run_time=2,rate_func=rate_functions.ease_out_sine)
        self.play(MoveAlongPath(dot,al3), run_time=1.5)
        self.play(MoveAlongPath(dot,al4), run_time=1.5)
        self.play(MoveAlongPath(dot,al5), run_time=1.5)
        self.play(MoveAlongPath(dot,al6), run_time=1.5)
        self.play(MoveAlongPath(dot,al7), run_time=1.5)
        self.play(MoveAlongPath(dot,al8), run_time=0.7,rate_func=rate_functions.ease_in_sine)
        self.play(MoveAlongPath(dot,al81), run_time=2.5,rate_func=rate_functions.ease_out_sine)
        self.play(MoveAlongPath(dot,al9), run_time=1.5)

        #example
        self.play(FadeOut(dot))
        self.wait(1)
        dot.move_to(bdot8.get_center())
        self.play(FadeOut(CircText))
        self.play(FadeIn(ExampleText))
        self.play(FadeIn(Example))
        self.play(FadeIn(dot))
        self.play(MoveAlongPath(dot,al8), run_time=1,rate_func=rate_functions.ease_in_sine)
        self.play(MoveAlongPath(dot,al81), run_time=3,rate_func=rate_functions.ease_out_sine)
        self.play(MoveAlongPath(dot,al9), run_time=1.5)

        self.add_foreground_mobject(dot)
        self.wait(1)
        self.play(LoopGroupDots.animate.set_opacity(0.6), run_time=0.25)
        self.play(LoopGroupLines.animate.set_color(color=[GRAY]), run_time=0.25)
        self.play(CircGroupDots.animate.set_opacity(1),run_time=0.25)
        self.add(CircGroupLines)
        self.play(CircGroupLines.animate.set_color(color=[WHITE]), run_time=0.25)
        self.add(CircGroupDots)


        self.play(MoveAlongPath(dot,a1), run_time=2)
        self.play(MoveAlongPath(dot,a2), run_time=1.5,rate_func=rate_functions.ease_in_sine)
        self.play(MoveAlongPath(dot,a21), run_time=1.5,rate_func=rate_functions.ease_out_sine)

        self.wait()
