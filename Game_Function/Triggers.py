from enum import Enum


class Trigger(Enum):

    # single digits means

    Ignition = 0
    OnTurnStart = 1
    OnPrepEnter = 2
    OnWeatherChange = 3
    OnCreatureBuy = 4
    OnDevelopmentBuy = 5
    OnMagicBuy = 6
    OnBuildingSell = 7
    OnMagicSell = 8
    OnMonsterTribute = 9
    OnCardActivate = 10
    OnCardResolve = 11
    EndPrep = 12
    OnAttackEnter = 13
    OnMonsterAttack = 14
    AfterMonsterAttack = 15
    EndAttack = 16
    OnPostEnter = 17
    EndPost = 18
    OnCardPlace = 19
    OnEnterGrave = 20




