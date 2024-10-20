class Lore(Scene):
    def construct(self):
        text1 = Text("Visualizing WashU Shuttles",font_size=65)
        text7 = Text("Travis Kuo and Jeslyn Gao", font_size=25)
        text1.shift(UP)
        self.play(Write(text1))
        self.play(Write(text7))
        self.wait(2)
        self.remove(text1,text7)

        text2 = Text("We wanted to create this project so")
        text3 = Text("that new WashU students could more")
        text4 = Text("easily visualize the shuttle system," )
        text5 = Text("knowing the location of the stops and")
        text6 = Text("directions that the shuttles go in.")
 
        group = VGroup(text2, text3, text4, text5, text6).arrange(DOWN,buff = 0.5)
        self.play(Write(group), run_time=5)
        self.wait(4)
        self.play(FadeOut(group))

        textlol = Text("We got lost..........................")
        textlol2 = Text("A lot.................")
        textlol.shift(UP)
        textlol2.shift(DOWN)
        self.play(FadeIn(textlol))
        self.wait(2)
        self.play(FadeIn(textlol2))
        self.wait(2)
