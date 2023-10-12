def piramida():
    blocks.fill(TNT, pos(-5, 2, -5), pos(5, 2, 5), FillOperation.REPLACE)
    blocks.fill(TNT, pos(-4, 3, -4), pos(4, 3, 4), FillOperation.REPLACE)
    blocks.fill(TNT, pos(-3, 4, -3), pos(3, 4, 3), FillOperation.REPLACE)
    blocks.fill(TNT, pos(-2, 5, -2), pos(2, 5, 2), FillOperation.REPLACE)
    blocks.fill(TNT, pos(-1, 6, -1), pos(1, 6, 1), FillOperation.REPLACE)
    blocks.fill(TNT, pos(0, 7, 0), pos(0, 7, 0), FillOperation.REPLACE)
    player.say("działa")

player.on_chat("p", piramida)
