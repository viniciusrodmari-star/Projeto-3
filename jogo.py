class jogo:
    def __init__(self, idJogo, titulo, console, genero, publisher, developer, critic_score, totalSales, naSales, jpSales, palSales, otherSales, reakeaseDate):
        self.id            = idJogo
        self.titulo        = titulo       
        self.console       = console     
        self.genero        = genero      
        self.publisher     = publisher   
        self.developer     = developer   
        self.critic_score  = critic_score
        self.totalSales    = totalSales  
        self.naSales       = naSales     
        self.jpSales       = jpSales     
        self.palSales      = palSales    
        self.otherSales    = otherSales  
        self.reakeaseDate  = reakeaseDate

    def exibir(self):
        print(f'{self.id },{self.titulo },{self.console},{self.genero},{self.publisher },{self.developer  },{self.critic_score },{self.totalSales},{self.naSales},{self.jpSales},{self.palSales},{self.otherSales},{self.reakeaseDate}')

    def linha_backlog(self):
        return f'{self.id};{self.titulo};{self.console}'
    
    def linha_recentes(self):
        return f'{self.id};{self.titulo};{self.console}'
    
    
