
def parkadv(): 
    verb_infinitivo = input("Digite o verbo no infinitivo ")
    adj = input("Digite um adjetivo ")
    subst = input("Digite um substantivo ")
    number = input("Digite um numero ")
    place = input("Digite um lugar ")
    verb_gerundio = input("Digite um verbo no gerundio ")
    person_name = input("Digite um nome de pessoa ")
    objeto = input("Digite um objeto ")
    animal = input("Digite um animal ")
    expression = input("Digite uma expressão ")

    if place.endswith('a'):
        connectorPlace = 'Na'
    else:
        connectorPlace = 'No'
    
    if objeto.endswith('a'):
        connectorObjeto = 'Na'
    else:
        connectorObjeto = 'No'
    
    park = f"{connectorPlace} {place}, {person_name} decidiu {verb_infinitivo} com um balão {adj}. Ele levou {number} balões para se divertir com seus amigos. Enquanto estavam {verb_gerundio} pelo lugar, encontraram um {animal} que estava muito interessado {connectorObjeto} {objeto}. '{expression}', exclamou {person_name} ao ver o {animal} tentando pegar um {subst}. A diversão foi garantida!"
    return park

def misterio():
    verb_infinitivo = input("Digite o verbo no infinitivo ")
    adj = input("Digite um adjetivo ")
    subst = input("Digite um substantivo ")
    number = input("Digite um numero ")
    place = input("Digite um lugar ")
    verb_gerundio = input("Digite um verbo no gerundio ")
    person_name = input("Digite um nome de pessoa ")
    objeto = input("Digite um objeto ")
    animal = input("Digite um animal ")
    expression = input("Digite uma expressão ")

    st = f"{person_name} estava na biblioteca, lendo um livro {adj} que encontrou na prateleira. Enquanto estava {verb_gerundio} por mais pistas, um {animal} entrou pela janela. '{expression}', pensou {person_name}. Após {verb_infinitivo}, usou uma lupa para examinar cada detalhe do livro. O mistério se aprofundava a cada página!"
    return st

def st3():
    verb_infinitivo = input("Digite o verbo no infinitivo ")
    adj = input("Digite um adjetivo ")
    subst = input("Digite um substantivo ")
    number = input("Digite um numero ")
    place = input("Digite um lugar ")
    verb_gerundio = input("Digite um verbo no gerundio ")
    person_name = input("Digite um nome de pessoa ")
    objeto = input("Digite um objeto ")
    animal = input("Digite um animal ")
    expression = input("Digite uma expressão ")

    st3 = f"{person_name} decidiu {verb_infinitivo} um castelo {adj} na praia com seus amigos. Eles levaram {number} pás para ajudar. Enquanto estavam {verb_gerundio}, {animal} se aproximou e observou com curiosidade. '{expression}!', disse Carlos, animado, enquanto todos trabalhavam juntos."
    return st3