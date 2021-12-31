

# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define ch_shin = Character("신기한 형사",color="#5570b5")
define ch_soo = Character("어수선 교감",color="#b58a55")
define ch_cha = Character("고차원",color="#b5a555")
define ch_tae = Character("강태산",color="#b89c37")
define ch_ha = Character("은하수",color="#b555b3")
define ch_ma = Character("한마리",color="#8755b5") #색 없앨수도 있음..우선은 걍 넣어둔거

define ch_narrator=Character(None)


screen ppt_imagemap():
        imagemap:
            auto "ppt_%s.png"
            text "마리가 밤 새워 만든 PPT를 클릭해보자!":
                size 35
                yalign 0.9 xalign 0.45

            hotspot(129,174,298,164) action  Return("ppt") 
            hotspot(552,158,457,398) action Return("mary")

screen news_imagemap():
        imagemap:
            auto "news_%s.png"
            
            hotspot(173,59,637,605) action Return("news") 

# 여기에서부터 게임이 시작합니다.
label start:
   
    stop music #시작할때 배경음 끄기
    play music "audio/bensound-cute.mp3" volume 0.2 fadein 1.0 
    scene bg_white
    show bg_start_1 with dissolve

    pause

    show bg_start_2 with dissolve
    
    pause

    show bg_start_3 with dissolve

    pause

    show bg_start_4 with dissolve
    
    pause
    
    show bg_start_5 with dissolve
    
    pause

    scene bg_white

    show bg_start2_1 with dissolve

    pause

    show bg_start2_2 with dissolve
    
    pause

    show bg_start2_3 with dissolve

    pause

    show bg_start2_4 with dissolve
    
    pause
    

    scene bg_white
    play sound "audio/kira.mp3" volume 0.5
    show bg_start3_1 with wipeleft
    
    pause
    stop sound 
    scene bg_white
    show bg_start4_1 with dissolve
    
    pause

    show bg_start4_2 with dissolve

    pause

    show bg_start4_3 with dissolve
    
    pause

    show bg_start4_5 with dissolve
    
    pause

    show bg_start4_6 with dissolve

    pause

    show bg_start4_7 with dissolve
    
    pause

    stop music fadeout 2.0
    scene bg_start5_1

    pause

    show bg_start5_2 with dissolve
    play sound "audio/open.mp3"
    pause
    stop sound
    jump mains

    return

label mains:

    scene bg_main_1 with fade
    play music "audio/bensound-scifi.mp3" fadein 1.0 volume 0.2
    ch_ma "다들 왔네~" with dissolve
    ch_ma "모두 와줘서 고마워."
    ch_ma "너희들과 꼭 이야기하고 싶은 게 있어서 말이야."
    ch_tae "칠판에 저건 뭐야!"
    "'신기한 모자 연구소'라고 쓰여 있다." 
    "마리가 직접 적은 듯하다."
    ch_ma "난 예전부터 꼭 연구해보고 싶었어."
    ch_ma "그건 바로..."
    stop music fadeout 1.5

    scene bg_main_2 with fade 
    play sound "audio/dddz.mp3" volume 0.2
    pause
    ch_ma "신기한 선생님의 모자에 대해!" with dissolve
    stop sound
    ch_ma "정말 흥미롭지 않아?"
    ch_ma "신기했던 점이 한둘이 아니란 말이야."
    ch_tae "그냥 모자잖아..."
    ch_tae "그러고 보니, 매일 같은 모자만 쓰시긴 하지."
    ch_ha "맞아. 그냥 모자인데..."
    ch_ha "엄청 큰일인 줄 알고 걱정했단 말이야!"
    ch_cha "(마리 귀엽다~)"
    ch_cha "그냥 모자처럼 보이지만 아닐 수도 있지!"
    ch_cha "그렇지만, 나도 단순한 모자일 거라고 생각해."

    scene bg_main_3 with fade

    show ma special1 
    
    ch_ma "우선 내가 PPT를 준비했으니 봐줘!"
    ch_tae "농담인줄 알았는데 진지했구나."
    ch_cha "와, 이런 건 다 언제 준비했어?"

    show ma special2
    play sound "audio/piano.mp3" volume 0.3
    "마리가 갑자기 피곤해보인다."
    ch_ha "괜찮아?"
    ch_ma "하나도 안괜찮으니까 이걸 봐줘!"
    stop sound
    show ma special1 
    
    ch_ma "자 그럼 발표를 시작할게."
    
    $c_num=0
    jump ppt
    
    
    
    return

label ppt:
    call screen ppt_imagemap
    if _return == 'ppt':
        play sound"audio/pong.mp3" volume 0.5
        hide ma
        jump ppt2

    else:
        play sound"audio/pat.mp3" volume 0.5
        ch_ma "아이참, 나 말고 PPT를 클릭해 봐!"
        ch_cha "맞아맞아"
        $c_num+=1
        if c_num>5:
            play sound"audio/piano.mp3"
            ch_ma "왜 나를 그렇게 많이 눌렀어?"
        jump ppt
    
label ppt2:
    #ppt
    play music "audio/bensound-energy.mp3" fadein 1.0 volume 0.4
    scene bg_ppt_1 with fade
    pause
    ch_ma "첫 번째, 나무에 거꾸로 매달려 있어도 모자는 떨어지지 않았어." with dissolve
    ch_ma "이건 모자가 만유인력을 무시한다는 증거가 될 수 있지!"
    ch_cha "와, PPT가 엄청 과학적이네. 역시 CSI 다워." 
    ch_ma "너네도 다 과학 형사거든~"
    ch_ma "차원아 심지어 이건 네 분야잖아!"
    #ppt
    scene bg_ppt_2 with dissolve
    pause
    ch_ma "두 번째! 아무리 강한 바람이 불어도 모자는 벗겨지지 않아." 
    ch_ha "이거 차원이 구했을 때지? 정말 큰일 날 뻔 했어."
    ch_tae "맞아. 저체온증으로 죽을 수도 있었다고."
    ch_tae "지금 생각해도 아찔하네."
    #ppt 
    scene bg_ppt_3 with dissolve
    pause
    ch_ma "앗, 이 사진은 왜 들어가 있지!"
    ch_ma "잠결에 잘 못 넣었나 봐."
    ch_tae "마리야, 이 사진은 언제 찍은 거야?"
    ch_ma "체육대회 때..."
    ch_ma "부끄러우니까 빨리 넘어갈게."
    #ppt
    scene bg_ppt_4 with dissolve
    pause
    ch_ma "세 번째! 365일 같은 모자만 쓰시는데도 모자가 전혀 더러워지지 않아." 
    ch_cha "저 사진들은 어디서 구한 거야?"
    ch_ma "어형사님께 부탁했지~"
    ch_ma "별걸 다 조사한다면서 주셨어."
    #scene
    play sound"audio/toggle.mp3"
    scene bg_main_3 with fade
    show ma special1
    ch_ma "이상으로 발표를 마치겠습니다~"
    play sound"audio/clapping.mp3"
    "CSI 멤버들이 박수를 쳤다."
    ch_ha "좋은 발표였어~"
    hide ma
    scene bg_main_4 with fade
    show ma default
    ch_ma "너희 이런 모자에 대해 어떻게 생각해?"
    show ma serious
    ch_ma "뭔가 이상하지 않아?"
    ch_ma "참고로 나는..."
    show ma happy 
    play sound"audio/dddz.mp3" volume 0.5
    ch_ma "사실 신형사님의 본체는 모자였다고 생각해!"
    ch_ma "아니면 이런 현상을 설명할 수 없다고!"
    hide ma
    show tae surprised
    ch_tae "그럴 리 없잖아!"
    ch_tae "애니메이션에서 안경이 본체인 캐릭터를 본 적은 있지만"
    ch_tae "신형사님은 모자가 본체일 것 같지는 않아."
    ch_tae "신형사님이 다른 걸 쓰시는 걸 한 번도 본 적이 없어."
    show tae serious
    ch_tae "분명 엄청 더러워질 텐데, 그렇지 않은 걸 보면..."
    
    show tae default
    play sound"audio/bell.mp3" volume 0.5
    ch_tae "신형사님의 모자는 스스로 깨끗해질 거야!"
    
    hide tae
    show ha surprised
    ch_ha "그런 게... 시중에 있나?"
    show ha default
    ch_ha "있었다면 우리들도 이미 알았을 것 같은데."

    hide ha
    show tae serious 
    ch_tae "사실 그건 그래."
    show tae surprised
    ch_tae "가설을 한번 세워본 거야."

    hide tae
    show cha default
    ch_cha "같은 모자를 200개쯤 갖고 계실 수도 있겠다."
    hide cha
    show ha default
    ch_ha "모자를 벗으면 머리 모양이 이상할 수도 있겠어."
    hide ha
    "다음 중 가장 그럴듯한 가설은 무엇일까?"
    menu:
        "한마리":
            play sound"audio/pong.mp3" volume 0.5
            show ma special3
            ch_ma "음... 난 내 추리가 가장 그럴듯 하다고 생각해."
            hide ma
            show tae serious
            ch_tae "그게... 과학적으로 타당한 가설이야?"
            hide tae
            show ma default
            ch_ma "하긴. 그건 그렇지."
            hide ma
        "고차원":
            play sound"audio/pong.mp3" volume 0.5
            show ma special4
            ch_ma "음... 난 차원이의 추리가 가장 그럴듯 하다고 생각해."
            hide ma
            show cha surprised
            ch_cha "그런데 그러려면 모자만 두는 방이 따로 있어야겠다."
            ch_cha "모자 200개... 너무 많아."
            hide cha
        "강태산":
            play sound"audio/pong.mp3" volume 0.5
            show ma special5
            ch_ma "음... 난 태산이의 추리가 가장 그럴듯 하다고 생각해."
            hide ma
            show tae default
            ch_tae "그래? 그런 게 있다면 나도 갖고 싶다."
            ch_tae "깨끗해지는 모자를 응용한다면 깨끗해지는 옷도 만들 수 있겠어."
            hide tae
        "은하수":
            play sound"audio/pong.mp3" volume 0.5
            show ma special6
            ch_ma "음... 난 하수의 추리가 가장 그럴듯 하다고 생각해."
            hide ma
            show ha surprised
            ch_ha "그런데, 다른 게임 캐릭터도 비슷한 논쟁이 있었는데"
            ch_ha "결국엔 평범한 머리였어."
            show ha default
            ch_ha "신형사님도 엄청 특이한 머리는 아닐 거야."
            hide ha
    play sound"audio/toggle.mp3"
    scene bg_main_4 with fade
    show ma default
    ch_ma "여기서 더 이야기하는 건 의미가 없을 것 같아."
    show ma happy
    ch_ma "각자 더 연구해보도록 하자. 어때?"
    hide ma
    menu:
        "좋아":
            pass
        "정말 좋아":
            pass
    play sound"audio/pong.mp3" volume 0.5
    show ma happy
    ch_ma "좋지? 그럴 줄 알았어."
    ch_ma "정말 흥미로운 주제라고 생각했다고!"
    show ma surprised
    ch_ma "다 같이 연구하면 실마리를 찾을 수 있을 거야!"
    show ma happy
    play sound"audio/deng.mp3" volume 0.7
    "(싫다는 선택지가 없었는데...)"
    hide ma
    show cha happy
    ch_cha "아무튼 이 모자는 재밌는 부분이 많네."
    hide cha
    show ha surprised
    ch_ha "그러게. 마리는 진짜 똑똑하다!"
    show ha happy
    ch_ha "이런 재밌는 주제도 가져오고."
    hide ha
    show ma default
    ch_ma "고마워. 사건이 아닌 과학 이야기를 다같이 해보면 어떨까 싶었어."
    hide ma
    show cha default
    ch_cha "괜찮은 생각이네!"
    hide cha
    show ma happy
    play sound"audio/drum.mp3" volume 0.6
    ch_ma "그리고 이 모임의 이름은..."
    hide ma
    menu:
        "신기한 모자 연구소":
            play sound"audio/pong.mp3" volume 0.5
        "어수선 신발 연구소":
            play sound"audio/pong.mp3" volume 0.5
            show ma serious
            ch_ma "내 발표 듣긴 한 거야?"
        "공차심 축구공 연구소":
            play sound"audio/pong.mp3" volume 0.5
            show ma serious
            ch_ma "내 발표 듣긴 한 거야?"
    show ma default
    ch_ma "'신기한 모자 연구소'야!"
    hide ma
    show ha surprised
    ch_ha "그런데, 이건 연구소의 형태가 아닌걸?"
    hide ha
    show ma happy
    ch_ma "그건 그렇다..."
    show ma default
    ch_ma "그럼 이건 어떨까?"
    ch_ma "이건 동아리인데, 동아리 이름이 '신기한 모자 연구소'인거야!"
    hide ma
    show cha surprised
    ch_cha "우린 4명인데 4명이 다 모이면 동아리가 아니라 반 모임 아니야?"
    hide cha
    show tae surprised
    play sound"audio/bell.mp3"
    ch_tae "논리적이야!"
    ch_ma "그렇지만 중요한 건 그게 아니니까!"
    hide tae
    show ma default
    ch_ma "암튼 이 모임은 신기한 모자 연구소야~ 어때?"
    ch_ha "좋아~"
    ch_cha "멋진 이름이네."
    hide ma
    show tae serious
    play sound"audio/deng.mp3"
    ch_tae "(선생님은 모르고 계셨으면 좋겠다...)"
    hide tae
    stop music fadeout 1.5
    #scene fade
    
    scene bg_white with fade
    show bg_main_5 with dissolve
    pause

    show bg_main_6 with dissolve
    
    pause
    "그렇게 우리는 틈틈이 모여 여러 가설을 세워 실험했다."   with dissolve
    "열심히 실험하던 와중에 입소문을 타고 동아리가 학교에서 유명해졌고,"
    "형사학교 신문에 인터뷰를 싣게 되었다."
    play sound "audio/toggle.mp3"
    scene bg_white with fade 
    play sound"audio/camera.mp3"
    "학생 기자" "이 동아리를 만들게 된 이유가 뭔가요?"
    show ma default
    ch_ma "제가 선생님의 모자를 보고 궁금한 점이 생겼는데,"
    ch_ma "CSI 친구들과 이것에 대해 얘기하면 재밌겠다 싶어서"
    ch_ma "친구들을 모아 동아리를 만들게 되었어요."
    hide ma
    play sound"audio/camera.mp3"
    "학생 기자" "선생님의 모자에 대한 비밀을 알게 되면 이 동아리의 목적을 달성하는 걸텐데요,"
    "학생 기자" "그 이후에 동아리의 행보에 대해 생각해둔 것이 있나요?"
    show ma surprised
    ch_ma "음... 아마 동아리를 해체하지 않을까요?"
    ch_ma "그렇지만 이 동아리의 목적은 모자의 진실을 알게 되는 것이 아니에요."
    ch_ma "사건 이야기로 가득 찬 24시간 중에"
    ch_ma "사건이 아닌 이야기를 하는 시간을 만든 거예요."
    show ma happy
    play sound"audio/pat.mp3"
    ch_ma "그건 바로 재밌는 과학 얘기죠!"
    hide ma
    jump mains2
    
    return

label mains2:
    scene black with fade
    "마리가 한 인터뷰는 학교 신문에 실리게 되었고,"
    "학생들 사이에서 소소하게 인기를 끌었다."

    scene bg_main2_1 with fade
    play music "audio/bensound-jazzyfrenchy.mp3" fadein 1.0
    "며칠 뒤, 형사 학교 도서관"
    play sound"audio/pat.mp3"
    show bg_main2_2 with dissolve
    pause
    
    scene bg_main2_3 with fade
    show shin serious
    ch_shin "어, 이게 뭐지?"
    #신문 확대

    hide shin 
    call screen news_imagemap
    play sound"audio/pong.mp3"
    show soo default 
    ch_soo "와~ 신형사도 이거 봤구나!"
    ch_soo "아이들이 재밌는 거 하더라고~"
    ch_soo "신형사에게 얘기 해줄까하다 말았지!"
    hide soo
    show shin default
    ch_shin "오, 재밌네요."
    ch_shin "제가 그 동아리에 들어가도 되는 걸까요?"
    ch_soo "답을 알려주면 재미없어하지 않을까?"
    show shin default2
    ch_shin "그러네요. 아이들이 알려달라고 하기 전까지는 가만히 있어야겠어요."
    hide shin
    play sound "audio/toggle.mp3"
    scene bg_start5_1 with fade
    stop music fadeout 1.5
    pause
    "몇 주 후, L201 강의실"
    scene bg_main_4 with fade
    play music "audio/March of the Spoons.mp3" fadein 1.0 volume 0.7
    show tae surprised
    ch_tae "진짜 모르겠어..."
    hide tae
    show ha surprised
    ch_ha "진짜 진짜 모르겠어..."
    hide ha
    show cha surprised
    ch_cha "지금까지 우리가 세운 가설들을 살펴보자!"
    play sound"audio/pong.mp3"
    "1. 모자는 선생님의 본체이다."
    "2. 모자가 스스로 깨끗해진다."
    "3. 모자를 벗으면 선생님의 머리 모양이 이상해진다."
    "4. 선생님은 같은 모자를 200개쯤 가지고 계신다."

    hide cha
    play sound "audio/knock.mp3"
    "똑똑..."

    "???" "여러분, 들어가도 되나요?"
    play sound "audio/toggle.mp3" volume 0.5
    scene bg_main_4 with fade
    show shin hat
    ch_shin "여러분, 원래는 답이 나올 때까지 기다리려고 했는데"
    ch_shin "몇 주 째 답이 나오지 않는 것 같아서 들어왔어요."
    hide shin
    show cha surprised
    ch_cha "3번 가설이 거짓으로 드러났어! 제일 그럴듯한 가설이었는데!"
    ch_tae "그게 중요한 게 아니야.. 선생님이 모자 벗으신 거 처음 보는 거라고!"
    hide cha
    show shin hat
    ch_shin "저의 모자와 관련된 이야기가 있어요. 들어주시겠어요?"
    hide shin
    
    # 과거 제시
    
    scene bg_white with fade
    play music "audio/bensound-adventure.mp3" fadein 1.0 volume 0.3
    show bg_main2_4 with dissolve
    pause
    show bg_main2_5 with dissolve
    pause
    show bg_main2_6 with dissolve
    pause
    show bg_main2_7 with dissolve
    play sound "audio/kira.mp3" volume 0.5
    pause
    show bg_main2_8 with dissolve 
    pause
    show bg_main2_9 with dissolve
    pause
    
    scene bg_main2_10 with fade
    play sound "audio/drum.mp3" volume 0.5
    pause
    stop sound
    scene bg_main2_11 with fade
    pause

    scene bg_white with dissolve
    show bg_main2_12 with dissolve
    pause
    show bg_main2_13 with dissolve
    pause
    show bg_main2_14 with dissolve
    pause
    show bg_main2_15 with dissolve
    pause
    show bg_main2_16 with dissolve

    pause
    


    scene bg_main_4 with fade 
    show ha sad
    ch_ha "그래서 소중하게 할 수 밖에 없는 모자라서..."
    ch_ha "선생님께 모자가 그렇게 중요한 존재인지 몰랐어요."
    ch_ha "그냥 어울려서 매일 쓰고 오신거라고 생각했는데..."
    hide ha
    show tae surprised
    ch_tae "정말 감동적이에요..."
    hide tae
    show cha happy
    ch_cha "선생님에 대한 새로운 이야기를 알게 되어 기뻐요."
    hide cha
    show ma surprised
    ch_ma "저희가 생각한 답은 아니지만,"
    show ma happy
    ch_ma "이 동아리를 하기 잘했다는 생각이 들어요!"
    ch_ma "일상에서 생긴 궁금증을 친구들과 함께 풀고, \n그 과정에서 여러 가지를 배울 수 있었어요."
    hide ma
    show shin hat2
    ch_shin "좋아요. 제가 여러분이 스스로 성장할 수 있는 계기가 되어서 기쁘네요."
    ch_shin "앞으로도 여러분들이 학교생활에서 많은 것을 배워갔으면 좋겠어요."
    hide shin

    scene black with fade
    "그 뒤로 모든 의문점은 해결되었고, ’신기한 모자 연구소‘는 자연스럽게 해체되었다." with dissolve
    "수사와 시험의 연속인 바쁜 학교생활 때문에 동아리는 점점 잊혀졌고,"
    "우리는 평범한 일상으로 돌아왔다."
    stop music fadeout 1.6
    jump ending
    
    return

label ending:
    scene bg_main2_1 with fade
    "어느 날, 형사 학교 도서관"
    call screen news_imagemap with dissolve
    play sound"audio/pong.mp3"
    scene bg_main2_3 with fade
    show tae surprised
    play music "audio/bensound-energy.mp3" fadein 1.0 volume 0.5
    ch_tae "어, 얘들아 이거 봐봐!"
    hide tae
    show ma surprised
    ch_ma "아 우리 이런 것도 했었지~"
    ch_ma "..."
    ch_ma "또 해봐도 재밌지 않을까?"

    hide ma
    scene bg_main_4 with fade
    "몇 주 후"
    show ma surprised
    ch_ma "어, 책상 위에 쪽지가 있네?"
    scene bg_main2_18 with dissolve
    stop music fadeout 1.5
    pause
    ch_ma "이거, 또 하자는 거겠지?" with dissolve
    
    play music "audio/bensound-sweet.mp3" fadein 1.0
    scene black with fade
    "'신기한 모자 연구소'는 잡다한 연구를 하는 동아리로 변경, \n지금도 그 행보를 이어나가고 있다." with dissolve
    jump credit
    return

label credit:
 
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The End", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide theend
    with dissolve
    with Pause(credits_speed - 5)
 

    ch_cha "그래서 이번에는 주제가 뭐라고?"
    ch_ha "난 계속 궁금했어..."
    ch_ha "책에 나오는 멍멍이는 어떻게 두 발로 걸을 수 있지?"
    ch_tae "...!"
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4)
    hide thanks
    with dissolve
    stop music fadeout 2.0
    return

init python:
    credits = ('제작','pyoumg'), ('사용 툴', 'Clip Studio pro'), ('사용 툴', 'Powerpoint')
    credits_s = "{size=80}신기한 모자 연구소\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=60}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=60}Engine\n{size=40}" + renpy.version()