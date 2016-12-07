def systemcheck():
    fullspeed()
    sleep(0.2)
    i01.setHeadSpeed(.75,.75)
    i01.moveHead(90,90)
    sleep(1)
    i01.moveHead(72,64)

    sleep(2)
    i01.moveHead(165,94)
    sleep(2)

    i01.moveHead(90,160)
    sleep(2)

    i01.moveHead(20,95)
    sleep(2)
    i01.moveHead(90,90)
    sleep(1.5)
    i01.mouth.speakBlocking("Head, neck and mouth,   check")
    sleep(1)
    i01.setHeadSpeed(.9,.9)
    i01.moveHead(25,61)
    i01.moveArm("left",0,90,30,10)
    i01.setArmSpeed("right",.75,.75,.75,.75)
    i01.moveArm("right",24,62,52,45)
    i01.moveHand("left",0,0,0,0,0,90)
    i01.moveHand("right",0,0,0,0,0,90)
    sleep(2)
    i01.moveHead(90,90)
    i01.setHeadSpeed(.9,.9)
    sleep(1)
    i01.mouth.speakBlocking("right arm and right shoulder,    check")
    sleep(1)
    i01.setHeadSpeed(.9,.9)
    i01.moveHead(20,122)
    i01.setArmSpeed("left",.75,.75,.75,.75)
    i01.moveArm("left",24,62,52,45)
    sleep(2)
    i01.moveHead(90,90)
    i01.setHeadSpeed(.9,.9)
    sleep(1)
    i01.mouth.speakBlocking("left arm and left shoulder,    check")
    sleep(1)
    i01.setHeadSpeed(.9,.9)
    i01.moveHead(20,120)

    i01.moveArm("left",75,123,52,45)
    i01.moveArm("right",75,123,52,45)
    i01.moveHand("left",180,180,180,180,180,30)
    i01.moveHand("right",180,180,180,180,180,170)
    sleep(3)
    i01.setHeadSpeed(.9,.9)
    i01.moveHead(59,67)

    i01.moveHand("right",0,0,0,0,0,19)
    i01.moveHand("left",0,0,0,0,0,170)
    sleep(1)
    i01.moveHand("left",180,180,180,180,180,30)
    i01.moveHand("right",180,180,180,180,180,170)
    sleep(1.5)
    i01.moveHead(90,90)
    i01.setHeadSpeed(.9,.9)
    sleep(1)
    i01.mouth.speakBlocking(" hands and Wrists,    check")
    sleep(1)

    i01.moveHead(90,90)
    i01.moveArm("left",0,90,30,10)
    i01.moveArm("right",0,90,30,10)
    i01.moveHand("left",0,0,0,0,0,90)
    i01.moveHand("right",0,0,0,0,0,90)
    i01.mouth.speakBlocking("all servos are functioning properly")
    sleep(1.5)
    i01.mouth.speakBlocking("awaiting your commands")
    sleep(0.5)
    relax()
