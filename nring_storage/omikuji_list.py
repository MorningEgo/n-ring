ngo = [
    "お布施してないんだから、当たらなくても文句言わないでよね！",
    "今日の気分は～・・・",
    "どれにしよっかな～",
    "なにがでるかな",
    "あっやべッ...！？",
    "ん、なに？おみくじ？　ん～じゃあこれで",
    "いいの出るといいね～",
    "おみくじの代わりにガムの包み紙じゃダメ？ダメか",
    "お！これはレアだよ～～～、とか言っとけば盛り上がる？",
    "お！　　　　...w",
    "どれが良いかな～",
    "おみくじって何回でも引き直していいんだって～",
    "お布施・・・",
    "よく当たるって噂になってます。お前以外",
    "今日のラスト一個だよ～！見てけ見てけ～～！！　・・・なんてね。"
]

jack_ngo = "行くぞ確定！！！！せーのっ！"


Key_Scale = [
    ["大　大　吉", 80, -1],
    ["大　吉", 64,79],
    ["中　吉", 50,63],
    ["小　吉", 40,49],
    ["吉", 30,39],
    ["凶", 19,29],
    ["大　凶", 1,18],
    ["大　大　凶", -1, 0]
]

Lucky_Weight = [
    12,
    11,
    9,
    8,
    7,
    6,
    7,
    8,
    9,
    11,
    12
]

Items = {
    "Wish":[
        "びっくりするほど叶わない\n考えるだけ無駄なので早く諦めること",
        "叶わない\n出直せ",
        "並外れた努力をしなければなにも叶わない\nつま先までラストチャンスに飢えること",
        "願事に対する気持ちが足りていない\n叶うものも叶わない",
        "いつでも叶うもの以外基本叶わない\n身の程を弁えて願うこと",
        "ちょっとよく分からないですね\n努力すれば良いんじゃないでしょうか",
        "穏やかに過ごせば少しは叶う\n欲を持ちすぎないように",
        "7割叶う\n3割に思いを馳せないこと",
        "叶うが選択を迫られる\n冷静に対処すること",
        "叶う\n座して待て",
        "より良い形で全て叶う\nすごいイイ感じになる"
    ],
    "Lost":[
        "もうどこにも無い\n考えるだけ無駄なので早く諦めること",
        "失くす方が悪い\n出直せ",
        "既に他人の物\n涙は拭くこと",
        "50年くらい探せば見つかる\n必死に探すこと",
        "実はもう見つけている\nださ",
        "ちょっとよく分からないですね\n探せば見つかるんじゃないですか",
        "近くにある\nたぶん気づかない",
        "ふとした時に見つかる\n但しその前により良いものが手に入る",
        "近々見つかる\n穏やかに待て",
        "必ず見つかる\n座して待て",
        "全て状態良く見つかる\nなんなら3倍くらいに増える"
    ],
    "Travel":[
        "行くも止めるも最悪の日になる\n考えるだけ無駄なので早く諦めること",
        "時期尚早である\n出直せ",
        "何とは言わないが\n止めたほうが吉となる",
        "旅先で失態に気付く\n帰りは修羅の道",
        "道中の苦労は計り知れない\n必ずどこかで人を頼ること",
        "ちょっとよく分からないですね\nよく調べればいいんじゃないですか",
        "収穫はあまり無い\n潔く諦めるのもまた吉",
        "今までの経験が物を言う\n過去に学んで歩むこと",
        "天候以外はほぼ全て良い\n雨具を忘れないこと",
        "実りのある旅路となる\n座して行け",
        "全てに恵まれた旅路となる\n好きなだけ欲を貪ること"]
    ,
    "Business":[
        "何も売れないし何を買おうにも損しかしない\n考えるだけ無駄なので早く諦めること",
        "その欲が身を滅ぼす\n出直せ",
        "簡単な事で騙され損をする\n気持ちを切り替えること",
        "売るほど得をするが買うほど損をする\n日を改めるも良し",
        "おおらかであるほど良くなる\nお布施を忘れれば修羅の道",
        "ちょっとよく分からないですね\n金銭感覚平気ならいいんじゃないですか",
        "一つの過ちで損得が逆転する\n取捨選択を誤らないこと",
        "時間をかけずに済ませること\n長考は運の尽きである",
        "無欲であるほどうまくいく\n常に穏やかであること",
        "時は金なり\n座して待て",
        "全部売れるしなんでも買い得\n私利私欲満たせ"
    ],
    "Study":[
        "今日ばっかりはのび太以下\n考えるだけ無駄なので早く諦めること",
        "判断が遅い\n出直せ",
        "何もできず踊るしかない\n踊る暇があったら勉強して",
        "少しの失念が命取りになる\n見直しを入念に",
        "本領発揮はできないが及第点\n予習復習を欠かさずに",
        "ちょっとよく分からないですね\n今までの積み重ね次第なんじゃないですか",
        "細かな所で気のゆるみが出る\n眠気覚ましを忘れずに",
        "目標に届くかは今日の努力次第\n焦らず着実に",
        "努力の成果が表れる\n但し油断しないこと",
        "今までの努力が実を結ぶ\n座して挑め",
        "頭が冴え、機転が利く\nエジソンもびっくりの自尊心を持って挑め"
    ],
    "Dispute":[
        "第三次大戦だ\n考えるだけ無駄なので早く諦めること",
        "修羅場\n出直せ",
        "悪化し増える\n耐え忍ぶ時",
        "増える\n行動を振り返ること",
        "まだ続く\n自身から切り出す必要有り",
        "ちょっとよく分からないですね\n喧嘩するほど仲が良いんじゃないですか",
        "もう少し続く\n相手は解決を望んでいる",
        "解決するが、靄が残る\n素直になること",
        "ちょっとした優しさで解決する\n自身から切り出すと吉",
        "時間が全てを解決する\n座して待て",
        "平和そのものとかの象徴となる\n✝︎昇天✝︎"
    ],
    "Draw":[
        "確定が外れるレベル\n考えるだけ無駄なので早く諦めること",
        "当たらん\n出直せ",
        "殆ど紙切れのみ\nなんか悪いことしました？",
        "相当のお布施が必要\n非課金は難しい",
        "本命は今日ではない\n育成せよ",
        "ちょっとよく分からないですね\n日頃の行いじゃないですか",
        "お布施しなければ本命は当たらない\n日を改めるのも吉",
        "いつもよりは当たる\n物欲を覗かれているので注意",
        "結構当たるがすり抜けやすい\n無心であれ",
        "よく当たる\n座して回せ",
        "ジャックポット\n壊れるまで回すべき"
    ],
    "Aim":[
        "…w\n考えるだけ無駄なので早く諦めること",
        "当たらん\n出直せ",
        "悪い癖が如実に出る\n他人の所為にしないこと",
        "普段より当たらない\n日を改めるのも吉",
        "悪くはないがあまり当たらない\n集中して練習をすること",
        "ちょっとよく分からないですね\n普段の練習次第なんじゃないですか",
        "普段通り\n高望みはしないように",
        "良いが隙が多い\n味方を信じること",
        "当たり良し\n深呼吸をして狙うこと",
        "ここぞという時に千里眼を得る\n座して撃て",
        "バチバチのプロ\n大会出たら？"
    ],
    "Direction":[
        "無",
        "北",
        "北北東",
        "北東",
        "東北東",
        "東",
        "東南東",
        "南東",
        "南",
        "南南西",
        "南西",
        "西南西",
        "西",
        "西北西",
        "北西",
        "北北西",
        "360°",
        "上",
        "下",
    ]
}

Key_Names = [
    "願事(ねがいごと)",
    "失物(うせもの)",
    "旅行(たびだち)",
    "商売(あきない)",
    "学問(がくもん)",
    "争事(あらそい)",
    "回事(がちゃ)",
    "当勘(あてかん)",
    "吉方(きっぽう)"
]