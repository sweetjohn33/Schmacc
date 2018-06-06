from enum import Enum


class Trigger(Enum):

    # single digits means

    NoTrig = 0
    OnDeath = 1
    OnAttackDec = 2
    Assist = 3
    AfterAttack = 4
    AfterDef = 5
    OnStandby = 6
    OnCardAct = 7
    Contin = 8


