# YI · 64 卦情境卡（文本版 spec v1）

每卡要素：编号 / 卦名卦象 / 一句话情境（中英） / 出处 / 爻变边 / 不适用（边界）。
本系列为**情境透镜，非占卜**：不预测吉凶，不输出行动建议。
爻变边由 `yi_engine.py` 二进制推导机器生成（已过 11 项封闭性/饱和性校验），禁止手改。
图片版待进卡片生产管线后补 image_url。

## YI01 乾 · 上乾下乾

一句话：天行不息——处在主动开局的时刻,凭自身力量把事情推起来,全场节奏由你定。
EN: Heaven in motion — you are opening the game, driving it forward on your own strength.
出处：《周易》第 1 卦
爻变：初九动→姤 YI44；九二动→同人 YI13；九三动→履 YI10；九四动→小畜 YI09；九五动→大有 YI14；上九动→夬 YI43
不适用：不预测开局能走多远,不回答该快该慢、该进该退。

## YI02 坤 · 上坤下坤

一句话：大地承载——处在顺势而为的位置,不抢头功,把别人的势接住、把事情托住。
EN: Earth that carries — you are in the supporting role, receiving momentum and holding things steady.
出处：《周易》第 2 卦
爻变：初六动→复 YI24；六二动→师 YI07；六三动→谦 YI15；六四动→豫 YI16；六五动→比 YI08；上六动→剥 YI23
不适用：不预测顺势能走多久,不回答该跟谁、该放手还是该接手。

## YI03 屯 · 上坎下震

一句话：万事开头难——想法有了,路还没走通,像草木破土,每一寸都在较劲。
EN: The hardest part is the beginning — the idea exists but the road isn't open yet, like sprouts pushing through soil.
出处：《周易》第 3 卦
爻变：初九动→比 YI08；六二动→节 YI60；六三动→既济 YI63；六四动→随 YI17；九五动→复 YI24；上六动→益 YI42
不适用：不预测难关何时过去,不回答该坚持还是该掉头。

## YI04 蒙 · 上艮下坎

一句话：蒙昧待启——面对的是不懂、不会、不开窍,需要有人点一下,或自己先交学费。
EN: Darkness before dawn — facing what you don't yet understand; someone must light the lamp, or you pay tuition to learn.
出处：《周易》第 4 卦
爻变：初六动→损 YI41；九二动→剥 YI23；六三动→蛊 YI18；六四动→未济 YI64；六五动→涣 YI59；上九动→师 YI07
不适用：不预测何时开窍,不回答该请教谁、该学还是该放。

## YI05 需 · 上坎下乾

一句话：密云不雨——时机没到,只能等,像等一场雨,急也没用,走也走不开。
EN: Clouds thick but no rain — the moment hasn't come; all you can do is wait, like waiting for rain.
出处：《周易》第 5 卦
爻变：初九动→井 YI48；九二动→既济 YI63；九三动→节 YI60；六四动→夬 YI43；九五动→泰 YI11；上六动→小畜 YI09
不适用：不预测要等多久,不回答该干等还是该做点别的。

## YI06 讼 · 上乾下坎

一句话：两边各执一词——处在争执里,公说公有理,讲不清,只能摆到台面上论。
EN: Two sides, each convinced they're right — you're in a dispute that can't be talked out privately.
出处：《周易》第 6 卦
爻变：初六动→履 YI10；九二动→否 YI12；六三动→姤 YI44；九四动→涣 YI59；九五动→未济 YI64；上九动→困 YI47
不适用：不预测谁输谁赢,不回答该争到底还是该让一步。

## YI07 师 · 上坤下坎

一句话：带队伍打硬仗——你不是一个人在战斗,身后有人,纪律和方向都得你来定。
EN: Leading troops into a hard fight — you're not alone; discipline and direction rest on you.
出处：《周易》第 7 卦
爻变：初六动→临 YI19；九二动→坤 YI02；六三动→升 YI46；六四动→解 YI40；六五动→坎 YI29；上六动→蒙 YI04
不适用：不预测仗打多久,不回答该攻该守、该赏该罚。

## YI08 比 · 上坎下坤

一句话：众人来亲附——处在被依靠、被靠近的位置,人心向你聚,关系网在成形。
EN: People drawing close — you are the one others lean on; a network is forming around you.
出处：《周易》第 8 卦
爻变：初六动→屯 YI03；六二动→坎 YI29；六三动→蹇 YI39；六四动→萃 YI45；九五动→坤 YI02；上六动→观 YI20
不适用：不预测人心能聚多久,不回答该亲近谁、该疏远谁。

## YI09 小畜 · 上巽下乾

一句话：小有积蓄,也小有阻滞——攒了点东西,但还不够,像云聚了,雨还没下。
EN: Small savings, small obstacles — you've gathered something, but not enough; clouds gather, rain hasn't fallen.
出处：《周易》第 9 卦
爻变：初九动→巽 YI57；九二动→家人 YI37；九三动→中孚 YI61；六四动→乾 YI01；九五动→大畜 YI26；上九动→需 YI05
不适用：不预测何时攒够,不回答该继续攒还是该先用。

## YI10 履 · 上乾下兑

一句话：如履薄冰——脚下是险处,每一步都得看准了踩,走得慢但走得稳。
EN: Treading on thin ice — every step must land sure; slow, but steady.
出处：《周易》第 10 卦
爻变：初九动→讼 YI06；九二动→无妄 YI25；六三动→乾 YI01；九四动→中孚 YI61；九五动→睽 YI38；上九动→兑 YI58
不适用：不预测冰面何时变厚,不回答该快走还是该绕路。

## YI11 泰 · 上坤下乾

一句话：天地交泰——上下通气,阻碍很少,像开春,万物都在生长。
EN: Heaven and earth in harmony — channels open, resistance low, like early spring when everything grows.
出处：《周易》第 11 卦
爻变：初九动→升 YI46；九二动→明夷 YI36；九三动→临 YI19；六四动→大壮 YI34；六五动→需 YI05；上六动→大畜 YI26
不适用：不预测顺境持续多久,不回答该扩张还是该收敛。

## YI12 否 · 上乾下坤

一句话：天地不交——上下不通,说什么都传不到,像被按了静音,各说各话。
EN: Heaven and earth apart — nothing gets through; it's like being muted, everyone talking past each other.
出处：《周易》第 12 卦
爻变：初六动→无妄 YI25；六二动→讼 YI06；六三动→遁 YI33；九四动→观 YI20；九五动→晋 YI35；上九动→萃 YI45
不适用：不预测闭塞何时打开,不回答该敲门还是该另找路。

## YI13 同人 · 上乾下离

一句话：和同道在一起——处在一群目标一致的人中间,方向相同,劲往一处使。
EN: Among fellow travelers — you're with people heading the same way, pulling together.
出处：《周易》第 13 卦
爻变：初九动→遁 YI33；六二动→乾 YI01；九三动→无妄 YI25；九四动→家人 YI37；九五动→离 YI30；上九动→革 YI49
不适用：不预测同行能走多远,不回答该跟谁结盟、该跟谁保持距离。

## YI14 大有 · 上离下乾

一句话：手里东西很多——处在丰盛的时刻,资源、机会、选择都不少,多到要分心。
EN: Hands full — a time of abundance; resources and options are plenty, enough to distract.
出处：《周易》第 14 卦
爻变：初九动→鼎 YI50；九二动→离 YI30；九三动→睽 YI38；九四动→大畜 YI26；六五动→乾 YI01；上九动→大壮 YI34
不适用：不预测丰盛持续多久,不回答该守成还是该再投。

## YI15 谦 · 上坤下艮

一句话：低调不吃亏——处在不张扬反而被接纳的位置,退一步,路反而宽。
EN: Low profile, wide road — humility opens doors here; stepping back creates space.
出处：《周易》第 15 卦
爻变：初六动→明夷 YI36；六二动→升 YI46；九三动→坤 YI02；六四动→小过 YI62；六五动→蹇 YI39；上六动→艮 YI52
不适用：不预测低调何时见效,不回答该藏多深、该露多少。

## YI16 豫 · 上震下坤

一句话：松弛的时光——处在安逸愉悦里,享受当下,但也容易忘了备后手。
EN: Easy times — relaxed and pleasant; enjoyment now, but vigilance tends to slip.
出处：《周易》第 16 卦
爻变：初六动→震 YI51；六二动→解 YI40；六三动→小过 YI62；九四动→坤 YI02；六五动→萃 YI45；上六动→晋 YI35
不适用：不预测安逸持续多久,不回答该及时行乐还是该未雨绸缪。

## YI17 随 · 上兑下震

一句话：跟着走——处在随从的位置,方向盘不在你手里,跟对人比走得快重要。
EN: Following — the wheel isn't in your hands; choosing whom to follow matters more than speed.
出处：《周易》第 17 卦
爻变：初九动→萃 YI45；六二动→兑 YI58；六三动→革 YI49；九四动→屯 YI03；九五动→震 YI51；上六动→无妄 YI25
不适用：不预测跟的人能走多远,不回答该跟还是该单飞。

## YI18 蛊 · 上艮下巽

一句话：屋子该整修了——处在积弊已久的局面,问题不是一天攒的,得一件件翻出来治。
EN: The house needs repair — long-accumulated problems; nothing formed overnight, each must be dug out and fixed.
出处：《周易》第 18 卦
爻变：初六动→大畜 YI26；九二动→艮 YI52；九三动→蒙 YI04；六四动→鼎 YI50；六五动→巽 YI57；上九动→升 YI46
不适用：不预测整修要花多久,不回答先治哪件、该大修还是小补。

## YI19 临 · 上坤下兑

一句话：走到跟前了——处在亲临一线的位置,事情近在眼前,看得见摸得着。
EN: Right at the front — you're close to the action; things are visible, tangible, within reach.
出处：《周易》第 19 卦
爻变：初九动→师 YI07；九二动→复 YI24；六三动→泰 YI11；六四动→归妹 YI54；六五动→节 YI60；上六动→损 YI41
不适用：不预测临近之后发生什么,不回答该亲力亲为还是该放手。

## YI20 观 · 上巽下坤

一句话：站在高处看——处在观察的位置,先看清楚全貌,不急着下场。
EN: Watching from above — in the observer's seat; see the whole picture before stepping in.
出处：《周易》第 20 卦
爻变：初六动→益 YI42；六二动→涣 YI59；六三动→渐 YI53；六四动→否 YI12；九五动→剥 YI23；上九动→比 YI08
不适用：不预测看出什么结论,不回答何时下场、该看多久。

## YI21 噬嗑 · 上离下震

一句话：骨头里有刺——处在硬骨头卡在中间的局面，有障碍横着，不咬碎就过不去。
EN: A bone stuck in the throat — an obstacle lodged across the path; it must be bitten through to move on.
出处：《周易》第 21 卦
爻变：初九动→晋 YI35；六二动→睽 YI38；六三动→离 YI30；九四动→颐 YI27；六五动→无妄 YI25；上九动→震 YI51
不适用：不预测硬骨头多难啃,不回答该硬啃还是该绕开。

## YI22 贲 · 上艮下离

一句话：讲究体面——处在重包装、重门面的时刻,里子有没有,面子先得有。
EN: Appearances matter — a time for polish and presentation; the surface must hold before anything else.
出处：《周易》第 22 卦
爻变：初九动→艮 YI52；六二动→大畜 YI26；九三动→颐 YI27；六四动→离 YI30；六五动→家人 YI37；上九动→明夷 YI36
不适用：不预测体面能撑多久,不回答该重里子还是该重面子。

## YI23 剥 · 上艮下坤

一句话：墙皮在剥落——处在东西一点点被剥掉的局面,根基还在被掏,得看住最后那点。
EN: Paint peeling off the wall — things being stripped away layer by layer; watch what remains.
出处：《周易》第 23 卦
爻变：初六动→颐 YI27；六二动→蒙 YI04；六三动→艮 YI52；六四动→晋 YI35；六五动→观 YI20；上九动→坤 YI02
不适用：不预测剥落何时见底,不回答该加固还是该放弃。

## YI24 复 · 上坤下震

一句话：触底回转——处在由衰转盛的当口,旧的走完了,新的刚冒头。
EN: The turn — at the pivot from decline to renewal; the old is spent, the new just sprouts.
出处：《周易》第 24 卦
爻变：初九动→坤 YI02；六二动→临 YI19；六三动→明夷 YI36；六四动→震 YI51；六五动→屯 YI03；上六动→颐 YI27
不适用：不预测回升有多快,不回答该加码还是该再看看。

## YI25 无妄 · 上乾下震

一句话：别瞎折腾——处在不妄动反而没事的局面,守住本分,不节外生枝。
EN: Don't stir trouble — a time when restraint keeps you safe; hold your ground, add nothing extra.
出处：《周易》第 25 卦
爻变：初九动→否 YI12；六二动→履 YI10；六三动→同人 YI13；九四动→益 YI42；九五动→噬嗑 YI21；上九动→随 YI17
不适用：不预测安分能保多久平安,不回答该守成还是该试探。

## YI26 大畜 · 上艮下乾

一句话：大仓满了——处在厚积的阶段,攒的东西够多,缺的是一个出手的时机。
EN: The granary is full — a phase of deep accumulation; plenty stored, waiting for the moment to act.
出处：《周易》第 26 卦
爻变：初九动→蛊 YI18；九二动→贲 YI22；九三动→损 YI41；六四动→大有 YI14；六五动→小畜 YI09；上九动→泰 YI11
不适用：不预测时机何时到,不回答该继续攒还是该出手。

## YI27 颐 · 上艮下震

一句话：养人养自己——处在靠供养运转的局面,养什么、被什么养,决定了长成什么样。
EN: Nourishment — everything runs on what feeds it; what you feed, and what feeds you, shapes what grows.
出处：《周易》第 27 卦
爻变：初九动→剥 YI23；六二动→损 YI41；六三动→贲 YI22；六四动→噬嗑 YI21；六五动→益 YI42；上九动→复 YI24
不适用：不预测养分够吃多久,不回答该养什么、该断什么粮。

## YI28 大过 · 上兑下巽

一句话：栋梁弯了——处在过度、非常规的局面,正常招式不够用,非常时期行非常事。
EN: The beam is bending — an excessive, extraordinary situation; ordinary moves won't do.
出处：《周易》第 28 卦
爻变：初六动→夬 YI43；九二动→咸 YI31；九三动→困 YI47；九四动→井 YI48；九五动→恒 YI32；上六动→姤 YI44
不适用：不预测非常态持续多久,不回答该撑住还是该换梁。

## YI29 坎 · 上坎下坎

一句话：一险接一险——处在险境连环的位置,刚出一坑又一坎,只能一关一关过。
EN: Danger upon danger — pit after pit; the only way is through, one at a time.
出处：《周易》第 29 卦
爻变：初六动→节 YI60；九二动→比 YI08；六三动→井 YI48；六四动→困 YI47；九五动→师 YI07；上六动→涣 YI59
不适用：不预测险境何时到头,不回答该硬闯还是该等水退。

## YI30 离 · 上离下离

一句话：火要附着东西烧——处在靠依附才能发光的位置,有明,但得有所附。
EN: Fire needs fuel to burn — brightness here depends on attachment; clarity exists, but it clings to something.
出处：《周易》第 30 卦
爻变：初九动→旅 YI56；六二动→大有 YI14；九三动→噬嗑 YI21；九四动→贲 YI22；六五动→同人 YI13；上九动→丰 YI55
不适用：不预测光明照多远,不回答该依附谁、该靠自己。

## YI31 咸 · 上兑下艮

一句话：心有感应——处在互相有感觉的时刻,还没挑明,但双方都接到了信号。
EN: A felt response — mutual signals not yet spoken aloud, but both sides have received them.
出处：《周易》第 31 卦
爻变：初六动→革 YI49；六二动→大过 YI28；九三动→萃 YI45；九四动→蹇 YI39；九五动→小过 YI62；上六动→遁 YI33
不适用：不预测感应通向哪里,不回答该挑明还是该再等等。

## YI32 恒 · 上震下巽

一句话：细水长流——处在靠恒久取胜的局面,不比爆发,比谁不断。
EN: The long steady stream — winning by endurance here, not by bursts; it's about who doesn't break.
出处：《周易》第 32 卦
爻变：初六动→大壮 YI34；九二动→小过 YI62；九三动→解 YI40；九四动→升 YI46；六五动→大过 YI28；上六动→鼎 YI50
不适用：不预测恒久能撑多久,不回答该加码还是该维持。

## YI33 遁 · 上乾下艮

一句话：该退了——处在退比进明智的时刻,不是认输,是留得青山。
EN: Time to step back — retreat is the wiser move now; not surrender, but keeping the mountain green.
出处：《周易》第 33 卦
爻变：初六动→同人 YI13；六二动→姤 YI44；九三动→否 YI12；九四动→渐 YI53；九五动→旅 YI56；上九动→咸 YI31
不适用：不预测退到何时能回,不回答该退多远、该带什么走。

## YI34 大壮 · 上震下乾

一句话：壮过头了——处在力量过盛的局面,劲大容易折,收着点反而走得远。
EN: Too strong — power in excess; great force snaps easily, holding back travels further.
出处：《周易》第 34 卦
爻变：初九动→恒 YI32；九二动→丰 YI55；九三动→归妹 YI54；九四动→泰 YI11；六五动→夬 YI43；上六动→大有 YI14
不适用：不预测盛极何时转衰,不回答该收敛还是该趁热。

## YI35 晋 · 上离下坤

一句话：往上走——处在被提拔、被看见的上升通道里,台阶在脚下,一级一级上。
EN: Moving up — in an ascending channel, seen and lifted; the steps are underfoot, one at a time.
出处：《周易》第 35 卦
爻变：初六动→噬嗑 YI21；六二动→未济 YI64；六三动→旅 YI56；九四动→剥 YI23；六五动→否 YI12；上九动→豫 YI16
不适用：不预测能升到哪一级,不回答该快上还是该稳扎。

## YI36 明夷 · 上坤下离

一句话：光被遮住了——处在明珠暗投的局面,有光但不能露,得藏着走。
EN: Light obscured — brightness that can't show itself; keep it hidden and move quietly.
出处：《周易》第 36 卦
爻变：初九动→谦 YI15；六二动→泰 YI11；九三动→复 YI24；六四动→丰 YI55；六五动→既济 YI63；上六动→贲 YI22
不适用：不预测黑暗持续多久,不回答该韬晦还是该冒险露光。

## YI37 家人 · 上巽下离

一句话：家里的事——处在以内治为主的局面,先把内部理顺,外面自然顺。
EN: Household matters — the inside must be set right first; order within, and the outside follows.
出处：《周易》第 37 卦
爻变：初九动→渐 YI53；六二动→小畜 YI09；九三动→益 YI42；六四动→同人 YI13；九五动→贲 YI22；上九动→既济 YI63
不适用：不预测家事何时理顺,不回答该严还是该宽。

## YI38 睽 · 上离下兑

一句话：看不对眼——处在互相乖离的局面,各看各不顺眼,话不投机。
EN: Seeing cross-eyed — mutual estrangement; neither side pleases the other, words don't land.
出处：《周易》第 38 卦
爻变：初九动→未济 YI64；九二动→噬嗑 YI21；六三动→大有 YI14；九四动→损 YI41；六五动→履 YI10；上九动→归妹 YI54
不适用：不预测乖离何时弥合,不回答该求同还是该分道。

## YI39 蹇 · 上坎下艮

一句话：前有水后有山——处在进退两难的位置,进也难,退也难,卡在中间。
EN: Water ahead, mountains behind — stuck between advance and retreat; both hard, caught in the middle.
出处：《周易》第 39 卦
爻变：初六动→既济 YI63；六二动→井 YI48；九三动→比 YI08；六四动→咸 YI31；九五动→谦 YI15；上六动→渐 YI53
不适用：不预测僵局何时打破,不回答该硬进还是该回头。

## YI40 解 · 上震下坎

一句话：绳结松了——处在紧张缓解的当口,绷着的劲在松,事情有了转圜。
EN: The knot loosens — tension easing; what's been taut is slackening, room to maneuver appears.
出处：《周易》第 40 卦
爻变：初六动→归妹 YI54；九二动→豫 YI16；六三动→恒 YI32；九四动→师 YI07；六五动→困 YI47；上六动→未济 YI64
不适用：不预测缓解能走多远,不回答该趁势推还是该歇一歇。

## YI41 损 · 上艮下兑

一句话：要割点肉——处在要做减法的局面，舍掉一部分，才能保住大头。
EN: Time to cut back — in a situation demanding reduction; give up a part to keep the whole.
出处：《周易》第 41 卦
爻变：初九动→蒙 YI04；九二动→颐 YI27；六三动→大畜 YI26；六四动→睽 YI38；六五动→中孚 YI61；上九动→临 YI19
不适用：不预测减损到何时见底,不回答该割哪块、割多深。

## YI42 益 · 上巽下震

一句话：有人添柴——处在得外力增益的局面,顺风来,东西在往多了长。
EN: Someone adds fuel — gaining from outside help; the wind is fair, things are growing.
出处：《周易》第 42 卦
爻变：初九动→观 YI20；六二动→中孚 YI61；六三动→家人 YI37；六四动→无妄 YI25；九五动→颐 YI27；上九动→屯 YI03
不适用：不预测增益持续多久,不回答该乘势扩还是该先稳住。

## YI43 夬 · 上兑下乾

一句话：到摊牌的时候了——处在非断不可的关口，拖不得，不断就乱。
EN: Showdown time — at a point where the break can't wait; delay breeds chaos.
出处：《周易》第 43 卦
爻变：初九动→大过 YI28；九二动→革 YI49；九三动→兑 YI58；九四动→需 YI05；九五动→大壮 YI34；上六动→乾 YI01
不适用：不预测决断后果如何,不回答该快刀还是该缓刀。

## YI44 姤 · 上乾下巽

一句话：不期而遇——处在意外相逢的局面,没约好,撞上了,后头怎么发展看造化。
EN: Chance encounter — an unplanned meeting; uninvited, it happened; what follows is unwritten.
出处：《周易》第 44 卦
爻变：初六动→乾 YI01；九二动→遁 YI33；九三动→讼 YI06；九四动→巽 YI57；九五动→鼎 YI50；上九动→大过 YI28
不适用：不预测相逢带来什么,不回答该深交还是该保持距离。

## YI45 萃 · 上兑下坤

一句话：人聚起来了——处在聚集的局面,人、物、事往一处拢,场子热起来了。
EN: Gathering — people, things, matters converging; the place is warming up.
出处：《周易》第 45 卦
爻变：初六动→随 YI17；六二动→困 YI47；六三动→咸 YI31；九四动→比 YI08；九五动→豫 YI16；上六动→否 YI12
不适用：不预测聚集后往哪去,不回答该聚拢还是该散开。

## YI46 升 · 上坤下巽

一句话：芝麻开花——处在节节上升的通道里,一步一台阶,稳着往上走。
EN: Steadily rising — step by step upward; the channel climbs, keep it steady.
出处：《周易》第 46 卦
爻变：初六动→泰 YI11；九二动→谦 YI15；九三动→师 YI07；六四动→恒 YI32；六五动→井 YI48；上六动→蛊 YI18
不适用：不预测上升到哪一层,不回答该加速还是该蓄力。

## YI47 困 · 上兑下坎

一句话：泽下有水,水被困住——资源还在,但流不动了。有能力、有存量,却被环境卡住,动弹不得。
EN: Water trapped beneath the marsh — the resource exists but cannot flow. Not empty, but stuck.
出处：《周易》第 47 卦
爻变：初六动→兑 YI58；九二动→萃 YI45；六三动→大过 YI28；九四动→坎 YI29；九五动→解 YI40；上六动→讼 YI06
不适用：不预测何时脱困,不回答该走该留、该攻该守。

## YI48 井 · 上坎下巽

一句话：一口井——处在养人的位置,水在那,不来打就没水喝,井养人,人也得护井。
EN: A well — in the position of nourishing others; the water is there, but only for those who draw; the well feeds people, people must tend the well.
出处：《周易》第 48 卦
爻变：初六动→需 YI05；九二动→蹇 YI39；九三动→坎 YI29；六四动→大过 YI28；九五动→升 YI46；上六动→巽 YI57
不适用：不预测井水何时见底,不回答该多打还是该省着用。

## YI49 革 · 上兑下离

一句话：要换天了——处在非变不可的关口,旧的那套转不动了,新规矩在路上。
EN: The old order is spent — change is unavoidable; the old ways no longer turn, new rules are on the way.
出处：《周易》第 49 卦
爻变：初九动→咸 YI31；六二动→夬 YI43；九三动→随 YI17；九四动→既济 YI63；九五动→丰 YI55；上六动→同人 YI13
不适用：不预测变革何时落地,不回答该快刀换还是该渐进改。

## YI50 鼎 · 上离下巽

一句话：立新鼎——处在除旧布新的局面,新架子搭起来了,等的是往里添东西。
EN: A new cauldron set up — the old cleared away, the new frame stands; now it waits to be filled.
出处：《周易》第 50 卦
爻变：初六动→大有 YI14；九二动→旅 YI56；九三动→未济 YI64；九四动→蛊 YI18；六五动→姤 YI44；上九动→恒 YI32
不适用：不预测新鼎何时立稳,不回答该添什么料、该旺火还是文火。

## YI51 震 · 上震下震

一句话：一声雷——处在突发震动的局面,地动了,所有人都得先站稳再说。
EN: A thunderclap — sudden shock; the ground moves, everyone must find footing first.
出处：《周易》第 51 卦
爻变：初九动→豫 YI16；六二动→归妹 YI54；六三动→丰 YI55；九四动→复 YI24；六五动→随 YI17；上六动→噬嗑 YI21
不适用：不预测震动持续几波,不回答该躲还是该迎上去。

## YI52 艮 · 上艮下艮

一句话：到此为止——处在该停的关口,动不如静,停下来,看清楚再说。
EN: Stop here — at the point where stillness beats motion; halt, see clearly, then decide.
出处：《周易》第 52 卦
爻变：初六动→贲 YI22；六二动→蛊 YI18；九三动→剥 YI23；六四动→旅 YI56；六五动→渐 YI53；上九动→谦 YI15
不适用：不预测要停多久,不回答该原地停还是该掉头。

## YI53 渐 · 上巽下艮

一句话：鸿雁南飞,一步一站——处在循序渐进的局面,急不得,按部就班自有到时。
EN: Wild geese flying south, one stop at a time — progress by order; no rushing, each stage in turn.
出处：《周易》第 53 卦
爻变：初六动→家人 YI37；六二动→巽 YI57；九三动→观 YI20；六四动→遁 YI33；九五动→艮 YI52；上九动→蹇 YI39
不适用：不预测何时到站,不回答该提速还是该守序。

## YI54 归妹 · 上震下兑

一句话：嫁得不对位——处在名分不正的结合里,凑合在一起,心里各有数。
EN: A mismatched union — joined without proper standing; together, but each knows the score.
出处：《周易》第 54 卦
爻变：初九动→解 YI40；九二动→震 YI51；六三动→大壮 YI34；九四动→临 YI19；六五动→兑 YI58；上六动→睽 YI38
不适用：不预测这段结合走多远,不回答该将就还是该散。

## YI55 丰 · 上震下离

一句话：日中则昃前——处在丰盛的顶点,东西多到满出来,但满就是转折的开始。
EN: At the peak of fullness — abundance overflowing; but fullness is where the turn begins.
出处：《周易》第 55 卦
爻变：初九动→小过 YI62；六二动→大壮 YI34；九三动→震 YI51；九四动→明夷 YI36；六五动→革 YI49；上六动→离 YI30
不适用：不预测顶点之后向哪转,不回答该趁满出手还是该守满。

## YI56 旅 · 上离下艮

一句话：人在旅途——处在寄人篱下的羁旅中,不是自己的地盘,行事得看人脸色。
EN: On the road — a sojourner on others' ground; not your territory, tread with care for hosts' moods.
出处：《周易》第 56 卦
爻变：初六动→离 YI30；六二动→鼎 YI50；九三动→晋 YI35；九四动→艮 YI52；六五动→遁 YI33；上九动→小过 YI62
不适用：不预测何时到家,不回答该安顿还是该继续走。

## YI57 巽 · 上巽下巽

一句话：风行无孔不入——处在靠渗透起作用的局面,不硬来,顺着缝往里走。
EN: Wind finds every crack — working by infiltration, not force; follow the seams inward.
出处：《周易》第 57 卦
爻变：初六动→小畜 YI09；九二动→渐 YI53；九三动→涣 YI59；六四动→姤 YI44；九五动→蛊 YI18；上九动→井 YI48
不适用：不预测渗透何时见效,不回答该进多深、该收多快。

## YI58 兑 · 上兑下兑

一句话：说说笑笑——处在和悦交流的场子里,气氛松,话易出口,事易商量。
EN: Laughter and talk — in a field of easy exchange; good mood, easy words, easy agreements.
出处：《周易》第 58 卦
爻变：初九动→困 YI47；九二动→随 YI17；六三动→夬 YI43；九四动→节 YI60；九五动→归妹 YI54；上六动→履 YI10
不适用：不预测和气持续多久,不回答该深谈还是该点到为止。

## YI59 涣 · 上巽下坎

一句话：一盘散沙——处在涣散的局面,人心散了,东西也在散,拢不起来。
EN: Scattered sand — dispersion; hearts drift, things drift, nothing holds together.
出处：《周易》第 59 卦
爻变：初六动→中孚 YI61；九二动→观 YI20；六三动→巽 YI57；六四动→讼 YI06；九五动→蒙 YI04；上九动→坎 YI29
不适用：不预测涣散何时到头,不回答该收拢还是该放手。

## YI60 节 · 上坎下兑

一句话：有度——处在讲节制的位置,该用用,该省省,分寸就是命。
EN: Measure — in the seat of restraint; spend where due, save where due; proportion is everything.
出处：《周易》第 60 卦
爻变：初九动→坎 YI29；九二动→屯 YI03；六三动→需 YI05；六四动→兑 YI58；九五动→临 YI19；上六动→中孚 YI61
不适用：不预测节制换来什么,不回答该紧还是该松。

## YI61 中孚 · 上巽下兑

一句话：心诚——处在以诚信立身的局面,信立住了,路自然有人让。
EN: Sincerity — standing on trust; once trust is established, the way opens on its own.
出处：《周易》第 61 卦
爻变：初九动→涣 YI59；九二动→益 YI42；六三动→小畜 YI09；六四动→履 YI10；九五动→损 YI41；上九动→节 YI60
不适用：不预测诚信何时见回报,不回答该信谁、该防谁。

## YI62 小过 · 上震下艮

一句话：小事可稍过，大事须收敛——处在宜小不宜大的局面，小处可越界，大处要守规矩。
EN: Small things may slightly exceed, great things must hold back — a time for small moves only.
出处：《周易》第 62 卦
爻变：初六动→丰 YI55；六二动→恒 YI32；九三动→豫 YI16；九四动→谦 YI15；六五动→咸 YI31；上六动→旅 YI56
不适用：不预测小过之后如何，不回答多小算过、多大算犯。

## YI63 既济 · 上坎下离

一句话：事成了——处在功成之后的局面,水已过河,但成了之后最容易松懈。
EN: Done — the work complete, the river crossed; but completion is when vigilance slips easiest.
出处：《周易》第 63 卦
爻变：初九动→蹇 YI39；六二动→需 YI05；九三动→屯 YI03；六四动→革 YI49；九五动→明夷 YI36；上六动→家人 YI37
不适用：不预测成局守多久,不回答该庆功还是该思危。

## YI64 未济 · 上离下坎

一句话：差一口气——处在还没成的局面,火候未到,路还长,但门没关。
EN: One breath short — not yet done; the moment isn't ripe, the road is long, but the door isn't shut.
出处：《周易》第 64 卦
爻变：初六动→睽 YI38；九二动→晋 YI35；六三动→鼎 YI50；九四动→蒙 YI04；六五动→讼 YI06；上九动→解 YI40
不适用：不预测何时能成,不回答该再等等还是该换条路。
