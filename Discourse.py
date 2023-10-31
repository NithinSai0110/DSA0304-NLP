class dis:
    def __init__(self,text):
        self.text=text
        self.chi=[]
    def add_child(self,chi_node):
        self.chi.append(chi_node)
        sen=["He need to buy car(s1)","He want to talk(s2)"]
        root=dis("Discourse Root")
        root.add_child(dis(sen[0]))
        root.add_child(dis(sen[1]))
        root.chi[0].add_child(root.chi(2))
        print(root)
