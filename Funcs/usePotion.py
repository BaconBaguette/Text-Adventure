##  Used in fightEnemy  ##
def usePotion(op, e, p):
    eff = p.effect.split('-')[0]
    val = int(p.effect.split('-')[1])

    if eff == 'heal':
        op.health += val
        print('You restore', val, 'health to yourself.')
        print()

    elif eff =='damage':
        e.health -= val
        print('You throw the', p.name, 'at the', e.name, ', dealing', val, 'damage.')
        print()

    op.inventory.remove(p)