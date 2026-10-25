# list.txt 歌曲导入报告

核查日期：2026-10-25。`list.txt` 保持原样，行号对应本次导入时的文件。

- 新增 361 首，保留原有 16 首，合计 377 首。
- 跳过 95 个重复条目（含原有歌曲及列表内重名、大小写和明显错字变体）。
- 跳过 5 个不能唯一确定的标题，详见下表。
- `爱言叶I-V` 展开为「愛言葉」「愛言葉Ⅱ」「愛言葉Ⅲ」「愛言葉Ⅳ」「愛言葉Ⅴ」。
- `88☆彡 深海少女` 拆为两首；「深海少女」与列表中更早的条目重复，未重复新增。
- 全部歌曲的七项评分均已清空；新增歌曲的 `difficulty` 和 `comments` 均为空。原有歌曲的其他数据和评论保留。
- 新增歌曲中，BPM 已填 326 首、留空 35 首；音高范围已填 216 首、留空 145 首。

## 来源与版本

歌曲的 `sources.metadata` 记录实际采用的 [VocaDB](https://vocadb.net/) 条目。制作人按条目的 Producer 信用记录，歌手按 Vocalist 信用记录；相同歌手的多个声库合并展示，重音テト的 UTAU 与 Synthesizer V 声库区分展示。
优先采用合成歌声录音；不同发布版本的元数据以各歌曲的来源链接为准。特别选择：右肩の蝶采用鏡音リン版；あの夏のいつかは采用初音ミク版；朧月采用巡音ルカ版；えれくとりっく・えんじぇぅ采用ヤスオ的初音ミク版；夜に駆ける及モア！ジャンプ！モア！采用初音ミク版。ray 保留人声与初音ミク共同演唱的信用记录。
BPM 先取对应 VocaDB 条目的记录，再用具体乐曲的谱面、节奏游戏资料和分析页面补充，链接见 `sources.bpm`。有明确变速记录时使用 `最小值~~最大值`，例如オツキミリサイタル的 `110~~195`、アディショナルメモリー的 `80~~200`。没有把来源间的分歧或半速/倍速差异直接当作变速区间。
音高范围参考 [音域データ! Wiki](https://w.atwiki.jp/saikouon_dokoda/pages/472.html)、[エンタメ中毒的歌曲音域表](https://entertainment-holic.com/range-of-vocaloid-popular-songs/) 及 [ミラクルボイス的历史音域表](https://rainbowvoice.blog103.fc2.com/blog-entry-23.html)，具体链接见 `sources.vocal_range`。这些是参考站点对录音的测量/转录，可能因主旋律、和声、装饰音及版本而不同。转为科学音高记法，如 mid1G → G3、mid2C → C4、hiC → C5、hihiC → C6。
没有找到足够明确的同一录音来源、存在互相冲突的数值、或只能找到其他翻唱/编曲版本的数据时，保持空白。空白不代表 0。

## 未导入：不能唯一确定的标题

| 行号 | 原始条目 | 原因与候选 |
| --- | --- | --- |
| 210 | 夏祭り | 同名の原曲・カバーが複数あり、JITTERIN’JINN / Whiteberry 系の曲か、ボカロの別曲かを特定できない。 [鬱P, ミナツキトーカ feat. 初音ミク](https://vocadb.net/S/38488)；[ぱぐねこP feat. 花響琴](https://vocadb.net/S/627321)；[Sum, まふまふ feat. 鏡音リン](https://vocadb.net/S/135294) |
| 232 | SOLEIL | トラボルタ「ソレイユ -Soleil-」と、てぃあら「Soleil」など複数候補がある。 [トラボルタ feat. 鏡音リン](https://vocadb.net/S/16240)；[てぃあら, Jun feat. 初音ミク](https://vocadb.net/S/41231)；[風音 feat. 鏡音レン Append (Serious)](https://vocadb.net/S/82357) |
| 291 | 冬の魔法 | *Luna と IIG など複数の同名オリジナル曲がある。 [*Luna, びび feat. 初音ミク](https://vocadb.net/S/221372)；[IIG feat. 初音ミク](https://vocadb.net/S/995)；[クヌースP feat. 初音ミク](https://vocadb.net/S/11428) |
| 368 | アイ | DECO*27、ATOLS など複数の同名曲がある。 [DECO＊27, Rockwell feat. 初音ミク](https://vocadb.net/S/215656)；[ATOLS feat. 初音ミク Append (Dark)](https://vocadb.net/S/32703)；[SABA.U1 feat. 巡音ルカ, 初音ミク Append (Sweet)](https://vocadb.net/S/526830) |
| 442 | Selfish | CircusP、*Luna、heart★breaker など複数の同名曲がある。 [サーカス feat. レオン, トニオ](https://vocadb.net/S/15640)；[heart★breaker feat. Ruby](https://vocadb.net/S/159591)；[40㍍P feat. 初音ミク](https://vocadb.net/S/4644) |

## 重复条目：已跳过

| 行号 | 原始条目 | 对应歌曲 | 原因 |
| --- | --- | --- | --- |
| 197 | 88☆彡 深海少女 | [深海少女](../data/songs/shinkai-shoujo.json) | リスト内の重複 |
| 202 | ねえねえねえ | [ねぇねぇねぇ。](../data/songs/nee-nee-nee.json) | リスト内の重複 |
| 204 | メルト | [メルト](../data/songs/melt.json) | 既存の歌曲 |
| 205 | CALC | [Calc.](../data/songs/calc.json) | リスト内の重複 |
| 206 | アスノョゾラ哨戒班 | [アスノヨゾラ哨戒班](../data/songs/asu-no-yozora-shoukaihan.json) | リスト内の重複 |
| 207 | 快晴 | [快晴](../data/songs/kaisei.json) | リスト内の重複 |
| 208 | ROLLING GIRL | [ローリンガール](../data/songs/rollin-girl.json) | リスト内の重複 |
| 209 | 六兆年と一夜物语 | [六兆年と一夜物語](../data/songs/rokuchounen-to-ichiya-monogatari.json) | 既存の歌曲 |
| 211 | 少女レイ | [少女レイ](../data/songs/shoujo-rei.json) | リスト内の重複 |
| 212 | TELL YOUR WORLD | [Tell Your World](../data/songs/tell-your-world.json) | 既存の歌曲 |
| 213 | 回る空うさぎ | [回る空うさぎ](../data/songs/mawaru-sora-usagi.json) | リスト内の重複 |
| 214 | 夜明けと蛍 | [夜明けと蛍](../data/songs/yoake-to-hotaru.json) | リスト内の重複 |
| 215 | 白い雪のプリンセスは | [白い雪のプリンセスは](../data/songs/shiroi-yuki-no-princess-wa.json) | リスト内の重複 |
| 216 | 夜もすがら君想ふ | [夜もすがら君想ふ](../data/songs/yomosugara-kimi-omou.json) | リスト内の重複 |
| 217 | ワルズエンドダンスホ... | [ワールズエンド・ダンスホール](../data/songs/world-s-end-dancehall.json) | リスト内の重複 |
| 218 | 妄想感伤代偿联盟 | [妄想感傷代償連盟](../data/songs/mousou-kanshou-daishou-renmei.json) | リスト内の重複 |
| 221 | ウミユリ海㡳谭 | [ウミユリ海底譚](../data/songs/umiyuri-kaitei-tan.json) | リスト内の重複 |
| 222 | シャルル | [シャルル](../data/songs/charles.json) | 既存の歌曲 |
| 223 | 里表ラバ一ズ | [裏表ラバーズ](../data/songs/uraomote-lovers.json) | リスト内の重複 |
| 225 | 幽霊東京 | [幽霊東京](../data/songs/yuurei-tokyo.json) | リスト内の重複 |
| 226 | ラグトレイン | [ラグトレイン](../data/songs/lagtrain.json) | リスト内の重複 |
| 227 | ココロ | [ココロ](../data/songs/kokoro.json) | リスト内の重複 |
| 228 | ヒビ力セ | [ヒビカセ](../data/songs/hibikase.json) | リスト内の重複 |
| 231 | からくりピエロ | [からくりピエロ](../data/songs/karakuri-pierrot.json) | 既存の歌曲 |
| 233 | 天乐 | [天樂](../data/songs/tengaku.json) | リスト内の重複 |
| 236 | セツナトリップ | [セツナトリップ](../data/songs/setsuna-trip.json) | リスト内の重複 |
| 237 | 悪ノ娘 | [悪ノ娘](../data/songs/aku-no-musume.json) | リスト内の重複 |
| 238 | 悪ノ召使 | [悪ノ召使](../data/songs/aku-no-meshitsukai.json) | 既存の歌曲 |
| 240 | FREELY TOMORROW | [FREELY TOMORROW](../data/songs/freely-tomorrow.json) | リスト内の重複 |
| 243 | バグ | [バグ](../data/songs/bug.json) | リスト内の重複 |
| 245 | FROM Y TO Y | [from Y to Y](../data/songs/from-y-to-y.json) | リスト内の重複 |
| 247 | MAGNET | [magnet](../data/songs/magnet.json) | リスト内の重複 |
| 256 | 东京テディベア | [東京テディベア](../data/songs/tokyo-teddy-bear.json) | リスト内の重複 |
| 263 | ブリキノダンス | [ブリキノダンス](../data/songs/buriki-no-dance.json) | 既存の歌曲 |
| 266 | ドラマッルギ | [ドラマツルギー](../data/songs/dramaturgy.json) | リスト内の重複 |
| 272 | echo | [ECHO](../data/songs/echo.json) | リスト内の重複 |
| 273 | 独りんぼエンヴィ | [独りんぼエンヴィー](../data/songs/hitorinbo-envy.json) | リスト内の重複 |
| 276 | みくみくにしてあげる | [みくみくにしてあげる♪【してやんよ】](../data/songs/miku-miku-ni-shite-ageru-shite-yan-yo.json) | リスト内の重複 |
| 278 | 妄想税 | [妄想税](../data/songs/mousouzei.json) | リスト内の重複 |
| 279 | 上弦の月 | [上弦の月](../data/songs/jougen-no-tsuki.json) | リスト内の重複 |
| 281 | ルカルカ | [ルカルカ★ナイトフィーバー](../data/songs/luka-lukanight-fever.json) | リスト内の重複 |
| 282 | 初めての恋が终わる时 | [初めての恋が終わる時](../data/songs/hajimete-no-koi-ga-owaru-toki.json) | リスト内の重複 |
| 287 | ツギハギスタッカート | [ツギハギスタッカート](../data/songs/tsugihagi-staccato.json) | リスト内の重複 |
| 289 | いーあるふぁんくらぶ | [いーあるふぁんくらぶ](../data/songs/yi-er-fanclub.json) | リスト内の重複 |
| 295 | dear | [Dear](../data/songs/dear.json) | リスト内の重複 |
| 296 | 星屑ユートピア | [星屑ユートピア](../data/songs/hoshikuzu-utopia.json) | リスト内の重複 |
| 297 | 神のまにまに | [神のまにまに](../data/songs/kami-no-manimani.json) | リスト内の重複 |
| 301 | いかないで | [いかないで](../data/songs/ikanaide.json) | リスト内の重複 |
| 304 | just be friends | [Just Be Friends](../data/songs/just-be-friends.json) | リスト内の重複 |
| 306 | rolling girl | [ローリンガール](../data/songs/rollin-girl.json) | リスト内の重複 |
| 316 | 君はできない子 | [君はできない子](../data/songs/kimi-wa-dekinai-ko.json) | リスト内の重複 |
| 317 | 愛して愛して愛して | [愛して愛して愛して](../data/songs/aishite-aishite-aishite.json) | リスト内の重複 |
| 324 | いろは唄 | [いろは唄](../data/songs/iroha-uta.json) | リスト内の重複 |
| 330 | ルマ | [ルマ](../data/songs/ruma.json) | リスト内の重複 |
| 331 | Bad ∞ End ∞ Night | [Bad ∞ End ∞ Night](../data/songs/bad-end-night.json) | リスト内の重複 |
| 332 | テレパシ | [テレパシ](../data/songs/telepathy.json) | リスト内の重複 |
| 333 | 腐れ外道とチョコレゐト | [腐れ外道とチョコレゐト](../data/songs/kusaregedou-to-chocolate.json) | リスト内の重複 |
| 335 | 二息歩行 | [二息歩行](../data/songs/nisoku-hokou.json) | リスト内の重複 |
| 337 | モニタリング | [モニタリング](../data/songs/monitoring.json) | リスト内の重複 |
| 340 | Tell Your World | [Tell Your World](../data/songs/tell-your-world.json) | 既存の歌曲 |
| 343 | ロキ | [ロキ](../data/songs/roki.json) | 既存の歌曲 |
| 344 | 混沌ブギ | [混沌ブギ](../data/songs/konton-boogie.json) | リスト内の重複 |
| 357 | アニマル | [アニマル](../data/songs/animal.json) | リスト内の重複 |
| 361 | ロミオとシンデレラ | [ロミオとシンデレラ](../data/songs/romeo-to-cinderella.json) | リスト内の重複 |
| 366 | ラヴィット | [ラヴィット](../data/songs/loveit.json) | リスト内の重複 |
| 370 | ODDS&ENDS | [ODDS&ENDS](../data/songs/odds-ends.json) | リスト内の重複 |
| 371 | ニア | [ニア](../data/songs/near.json) | リスト内の重複 |
| 372 | 恋愛裁判 | [恋愛裁判](../data/songs/renai-saiban.json) | 既存の歌曲 |
| 377 | ラビットホール | [ラビットホール](../data/songs/rabbit-hole.json) | リスト内の重複 |
| 380 | 惑星ループ | [惑星ループ](../data/songs/wakusei-loop.json) | リスト内の重複 |
| 381 | マトリョシカ | [マトリョシカ](../data/songs/matryoshka.json) | 既存の歌曲 |
| 382 | 炉心融解 | [炉心融解](../data/songs/roshin-yuukai.json) | リスト内の重複 |
| 383 | ゴーストルール | [ゴーストルール](../data/songs/ghost-rule.json) | リスト内の重複 |
| 391 | SPiCa | [SPiCa](../data/songs/spica.json) | リスト内の重複 |
| 393 | 独りんぼエンヴィー | [独りんぼエンヴィー](../data/songs/hitorinbo-envy.json) | リスト内の重複 |
| 400 | ホワイトハッピー | [ホワイトハッピー](../data/songs/white-happy.json) | リスト内の重複 |
| 403 | 神っぽいな | [神っぽいな](../data/songs/kamippoi-na.json) | リスト内の重複 |
| 406 | 乙女解剖 | [乙女解剖](../data/songs/otome-kaibou.json) | 既存の歌曲 |
| 407 | オレンジ | [オレンジ](../data/songs/orange.json) | リスト内の重複 |
| 410 | オツキミリサイタル | [オツキミリサイタル](../data/songs/otsukimi-recital.json) | リスト内の重複 |
| 411 | Henceforth | [Henceforth](../data/songs/henceforth.json) | リスト内の重複 |
| 414 | 如月アテンション | [如月アテンション](../data/songs/kisaragi-attention.json) | リスト内の重複 |
| 415 | サマータイムレコード | [サマータイムレコード](../data/songs/summertime-record.json) | リスト内の重複 |
| 418 | 劣等上等 | [劣等上等](../data/songs/rettou-joutou.json) | リスト内の重複 |
| 419 | KING | [KING](../data/songs/king.json) | 既存の歌曲 |
| 420 | 六兆年と一夜物語 | [六兆年と一夜物語](../data/songs/rokuchounen-to-ichiya-monogatari.json) | 既存の歌曲 |
| 426 | テトリス | [テトリス](../data/songs/tetoris.json) | リスト内の重複 |
| 431 | オーバーライド | [オーバーライド](../data/songs/override.json) | リスト内の重複 |
| 437 | ハウトゥー世界征服 | [ハウトゥー世界征服](../data/songs/how-to-sekai-seifuku.json) | リスト内の重複 |
| 444 | だれかの心臓になれたなら | [だれかの心臓になれたなら](../data/songs/dareka-no-shinzou-ni-nareta-nara.json) | リスト内の重複 |
| 445 | 透明エレジー | [透明エレジー](../data/songs/toumei-elegy.json) | リスト内の重複 |
| 448 | QUEEN | [QUEEN](../data/songs/queen.json) | リスト内の重複 |
| 449 | 天ノ弱 | [天ノ弱](../data/songs/amanojaku.json) | 既存の歌曲 |
| 450 | ドーナツホール | [ドーナツホール](../data/songs/donut-hole.json) | 既存の歌曲 |
| 455 | きゅうくらりん | [きゅうくらりん](../data/songs/kyuukurarin.json) | リスト内の重複 |

## 标题订正及展开

仅列出首次新增时与输入不同的标题；重复行的拼写变体见上表。未改写 `list.txt`。

| 行号 | 原始条目 | 导入标题 |
| --- | --- | --- |
| 4 | ハロ/ハワユ | [ハロ／ハワユ](../data/songs/hello-how-are-you.json) |
| 9 | 命に嫌われている | [命に嫌われている。](../data/songs/inochi-ni-kirawarete-iru.json) |
| 11 | みくみくにしてあげる♪ | [みくみくにしてあげる♪【してやんよ】](../data/songs/miku-miku-ni-shite-ageru-shite-yan-yo.json) |
| 25 | Just be friends | [Just Be Friends](../data/songs/just-be-friends.json) |
| 26 | ハロー、プラネット。 | [＊ハロー、プラネット。](../data/songs/hello-planet.json) |
| 60 | rain stops,good- | [rain stops, good-bye](../data/songs/rain-stops-good-bye.json) |
| 68 | エゴロック | [エゴロック](../data/songs/ego-rock.json) |
| 90 | パメラ | [パメラ](../data/songs/pamela.json) |
| 111 | 阿吽のビーツ | [阿吽のビーツ](../data/songs/aun-no-beats.json) |
| 127 | ODDS＆ENDS | [ODDS&ENDS](../data/songs/odds-ends.json) |
| 159 | shake it! | [shake it！](../data/songs/shake-it.json) |
| 197 | 88☆彡 深海少女 | [88☆彡](../data/songs/vocadb-400359.json) |
| 199 | 胧月 | [朧月](../data/songs/oborodzuki.json) |
| 201 | 爱言叶I-V | [愛言葉](../data/songs/ai-kotoba.json) |
| 201 | 爱言叶I-V | [愛言葉Ⅱ](../data/songs/ai-kotoba-ii.json) |
| 201 | 爱言叶I-V | [愛言葉Ⅲ](../data/songs/ai-kotoba-iii.json) |
| 201 | 爱言叶I-V | [愛言葉Ⅳ](../data/songs/ai-kotoba-iv.json) |
| 201 | 爱言叶I-V | [愛言葉Ⅴ](../data/songs/ai-kotoba-v.json) |
| 220 | PARANOIA | [paranoia](../data/songs/paranoia.json) |
| 224 | ホワイトハッピ一 | [ホワイトハッピー](../data/songs/white-happy.json) |
| 229 | 仆は初音ミクとキスをした | [僕は初音ミクとキスをした](../data/songs/boku-wa-hatsune-miku-to-kiss-o-shita.json) |
| 230 | ハロ一セカイ | [ハローセカイ](../data/songs/hello-sekai.json) |
| 239 | 梦と叶桜 | [夢と葉桜](../data/songs/yume-to-hazakura.json) |
| 246 | 星屑ユ一トピア | [星屑ユートピア](../data/songs/hoshikuzu-utopia.json) |
| 248 | 番风 | [番凩](../data/songs/tsugai-kogarashi.json) |
| 249 | 世界寿命と最后の一日 | [世界寿命と最後の一日](../data/songs/sekai-jumyou-to-saigo-no-ichinichi.json) |
| 250 | BLACK BOARD | [Black Board](../data/songs/black-board.json) |
| 254 | 心拍数#0822 | [心拍数♯0822](../data/songs/shinpakusuu-0822.json) |
| 255 | LETTER SONG | [letter song](../data/songs/letter-song.json) |
| 257 | 日常と地球の额縁 | [日常と地球の額縁](../data/songs/nichijou-to-chikyuu-no-gakubuchi.json) |
| 261 | レッドパジ | [レッド・パージ！！！](../data/songs/red-purge.json) |
| 262 | 蜘蛛糸モノポリ一 | [蜘蛛糸モノポリー](../data/songs/kumo-ito-monopoly.json) |
| 267 | ドリ一ムレス・ドリ一ムス | [ドリームレス・ドリームス](../data/songs/dreamless-dreams.json) |
| 269 | 白雪 ~sirayuki | [白雪～shirayuki～](../data/songs/snow-white.json) |
| 299 | 死别 | [死別](../data/songs/shibetsu.json) |
| 303 | されなくても君がいる | [愛されなくても君がいる](../data/songs/aisarenakute-mo-kimi-ga-iru.json) |
| 309 | その一秒 スローモーション | [その一秒スローモーション](../data/songs/sono-ichibyou-slow-motion.json) |
| 329 | 1/6 | [1/6 -out of the gravity-](../data/songs/1-6-out-of-the-gravity.json) |
| 350 | 空奏列车 | [空奏列車](../data/songs/kuusou-ressha.json) |
| 353 | 39みゅーじっく | [39みゅーじっく!](../data/songs/39-music.json) |
| 354 | Empurple | [エンパープル](../data/songs/empurple.json) |
| 362 | 缲り返し一粒 | [繰り返し一粒](../data/songs/kurikaeshi-hitotsubu.json) |
| 365 | モア！ジャンプ！モア | [モア！ジャンプ！モア！](../data/songs/more-jump-more.json) |
| 374 | こちら、幸福安心委員会です | [こちら、幸福安心委員会です。](../data/songs/kochira-koufuku-anshin-iinkai-desu.json) |
| 378 | Zero Talking | [ゼロトーキング](../data/songs/zero-talking.json) |
| 379 | 好き！雪！本気 | [好き！雪！本気マジック](../data/songs/suki-yuki-maji-magic.json) |
| 425 | おべか | [おべか](../data/songs/obeka.json) |
| 428 | Liar Dancer | [ライアーダンサー](../data/songs/liar-dancer.json) |
| 440 | 怪盗・洼园チヨコは絶対ミスらない | [怪盗・窪園チヨコは絶対ミスらない](../data/songs/kaitou-kubozono-chiyoko-wa-zettai-misuranai.json) |
| 453 | 強風オールバック | [強風オールバック](../data/songs/kyoufuu-all-back.json) |

## 留空的元数据

以下只列新增歌曲；BPM 已逐曲检索补充，音高范围已核对上述曲目表。未填字段可在之后找到匹配录音的可靠资料后补充。

| 歌曲 | 留空字段 |
| --- | --- |
| [エイリアンエイリアン](../data/songs/alien-alien.json) | 音高范围 |
| [パンダヒーロー](../data/songs/panda-hero.json) | 音高范围 |
| [心做し](../data/songs/kokoronashi.json) | 音高范围 |
| [Dear](../data/songs/dear.json) | 音高范围 |
| [ローリンガール](../data/songs/rollin-girl.json) | 音高范围 |
| [フォニイ](../data/songs/phony.json) | 音高范围 |
| [アンドロイドガール](../data/songs/android-girl.json) | 音高范围 |
| [コールボーイ](../data/songs/call-boy.json) | BPM |
| [右肩の蝶](../data/songs/migikata-no-chou.json) | 音高范围 |
| [rain stops, good-bye](../data/songs/rain-stops-good-bye.json) | 音高范围 |
| [夜明けと蛍](../data/songs/yoake-to-hotaru.json) | 音高范围 |
| [シンデレラ](../data/songs/cinderella.json) | 音高范围 |
| [ダーリンダンス](../data/songs/darling-dance.json) | 音高范围 |
| [告白ライバル宣言](../data/songs/kokuhaku-rival-sengen.json) | BPM |
| [二息歩行](../data/songs/nisoku-hokou.json) | 音高范围 |
| [神っぽいな](../data/songs/kamippoi-na.json) | 音高范围 |
| [パラジクロロベンゼン](../data/songs/paradichlorobenzene.json) | 音高范围 |
| [カレシのジュード](../data/songs/kareshi-no-jude.json) | 音高范围 |
| [お気に召すまま](../data/songs/oki-ni-mesu-mama.json) | 音高范围 |
| [ジャンキーナイトタウンオーケストラ](../data/songs/junky-night-town-orchestra.json) | 音高范围 |
| [ぼくらの16bit戦争](../data/songs/bokura-no-16bit-wars.json) | 音高范围 |
| [FREELY TOMORROW](../data/songs/freely-tomorrow.json) | 音高范围 |
| [メンタルチェンソー](../data/songs/mental-chainsaw.json) | 音高范围 |
| [p.h.](../data/songs/p-h.json) | 音高范围 |
| [魔法少女とチョコレゐト](../data/songs/mahou-shoujo-to-chocolate.json) | 音高范围 |
| [告白予行練習](../data/songs/kokuhaku-yokou-renshuu.json) | BPM |
| [ピエロ](../data/songs/pierrot.json) | 音高范围 |
| [臨界ダイバー](../data/songs/rinkai-diver.json) | BPM |
| [爆笑](../data/songs/bakushou.json) | 音高范围 |
| [きゅうくらりん](../data/songs/kyuukurarin.json) | 音高范围 |
| [ECHO](../data/songs/echo.json) | 音高范围 |
| [ヤンキーボーイ・ヤンキーガール](../data/songs/yankee-boy-yankee-girl.json) | BPM、音高范围 |
| [トゥインクル](../data/songs/twinkle.json) | BPM |
| [shake it！](../data/songs/shake-it.json) | 音高范围 |
| [シャンティ](../data/songs/shanti.json) | 音高范围 |
| [金曜日のおはよう-another story-](../data/songs/kinyoubi-no-ohayou-another-story.json) | BPM、音高范围 |
| [君はできない子](../data/songs/kimi-wa-dekinai-ko.json) | BPM、音高范围 |
| [人マニア](../data/songs/hito-mania.json) | 音高范围 |
| [悪魔の踊り方](../data/songs/akuma-no-odorikata.json) | 音高范围 |
| [ペテン師が笑う頃に](../data/songs/petenshi-ga-warau-koro-ni.json) | 音高范围 |
| [キライ・キライ・ジガヒダイ！](../data/songs/kirai-kirai-jiga-hidai.json) | 音高范围 |
| [骸骨楽団とリリア](../data/songs/gaikotsu-gakudan-to-lilia.json) | 音高范围 |
| [上弦の月](../data/songs/jougen-no-tsuki.json) | 音高范围 |
| [IMITATION BLACK](../data/songs/imitation-black.json) | BPM |
| [花弁、それにまつわる音声](../data/songs/kaben-sore-ni-matsuwaru-onsei.json) | 音高范围 |
| [Bad ∞ End ∞ Night](../data/songs/bad-end-night.json) | BPM、音高范围 |
| [Leia - Remind](../data/songs/leia-remind.json) | 音高范围 |
| [あの夏のいつかは](../data/songs/ano-natsu-no-itsuka-wa.json) | BPM、音高范围 |
| [朧月](../data/songs/oborodzuki.json) | BPM、音高范围 |
| [愛言葉Ⅲ](../data/songs/ai-kotoba-iii.json) | 音高范围 |
| [愛言葉Ⅴ](../data/songs/ai-kotoba-v.json) | 音高范围 |
| [白ゆき](../data/songs/shirayuki.json) | 音高范围 |
| [paranoia](../data/songs/paranoia.json) | 音高范围 |
| [ホワイトハッピー](../data/songs/white-happy.json) | 音高范围 |
| [僕は初音ミクとキスをした](../data/songs/boku-wa-hatsune-miku-to-kiss-o-shita.json) | 音高范围 |
| [ハローセカイ](../data/songs/hello-sekai.json) | 音高范围 |
| [アカツキアライヴァル](../data/songs/akatsuki-arrival.json) | 音高范围 |
| [番凩](../data/songs/tsugai-kogarashi.json) | 音高范围 |
| [世界寿命と最後の一日](../data/songs/sekai-jumyou-to-saigo-no-ichinichi.json) | 音高范围 |
| [Black Board](../data/songs/black-board.json) | 音高范围 |
| [祝福のメシアとアイの塔](../data/songs/shukufuku-no-messiah-to-ai-no-tou.json) | BPM、音高范围 |
| [letter song](../data/songs/letter-song.json) | 音高范围 |
| [日常と地球の額縁](../data/songs/nichijou-to-chikyuu-no-gakubuchi.json) | 音高范围 |
| [君恋し](../data/songs/kimi-koishi.json) | 音高范围 |
| [パズル](../data/songs/puzzle.json) | 音高范围 |
| [四季折の羽](../data/songs/shikiori-no-hane.json) | 音高范围 |
| [レッド・パージ！！！](../data/songs/red-purge.json) | BPM、音高范围 |
| [蜘蛛糸モノポリー](../data/songs/kumo-ito-monopoly.json) | 音高范围 |
| [帝国少女](../data/songs/teikoku-shoujo.json) | 音高范围 |
| [マリーの架空世界](../data/songs/marry-no-kakuu-sekai.json) | BPM、音高范围 |
| [白雪～shirayuki～](../data/songs/snow-white.json) | 音高范围 |
| [沈みゆく哀](../data/songs/shizumi-yuku-ai.json) | BPM、音高范围 |
| [罪の名前](../data/songs/tsumi-no-namae.json) | 音高范围 |
| [D/N/A](../data/songs/d-n-a.json) | 音高范围 |
| [君が生まれた日](../data/songs/kimi-ga-umareta-hi.json) | 音高范围 |
| [Yellow](../data/songs/yellow.json) | 音高范围 |
| [nuit](../data/songs/night.json) | 音高范围 |
| [ほころび](../data/songs/hokorobi.json) | 音高范围 |
| [glow](../data/songs/glow.json) | 音高范围 |
| [ニア](../data/songs/near.json) | 音高范围 |
| [ド屑](../data/songs/dokuzu.json) | 音高范围 |
| [オノマトペメガネ](../data/songs/onomatopoeia-megane.json) | BPM、音高范围 |
| [死別](../data/songs/shibetsu.json) | BPM、音高范围 |
| [花めづる君](../data/songs/hanamezuru-kimi.json) | BPM、音高范围 |
| [39](../data/songs/vocadb-14480.json) | 音高范围 |
| [Blessing](../data/songs/blessing.json) | 音高范围 |
| [空に免じて](../data/songs/sora-ni-menjite.json) | 音高范围 |
| [アリスブルー](../data/songs/alice-blue.json) | BPM、音高范围 |
| [その一秒スローモーション](../data/songs/sono-ichibyou-slow-motion.json) | 音高范围 |
| [群青讃歌](../data/songs/gunjou-sanka.json) | 音高范围 |
| [ファシネイター](../data/songs/fascinator.json) | 音高范围 |
| [ARiA](../data/songs/aria.json) | 音高范围 |
| [僕のサイノウ](../data/songs/boku-no-sainou.json) | 音高范围 |
| [Catch the Wave](../data/songs/catch-the-wave.json) | 音高范围 |
| [電波中毒ガール](../data/songs/denpa-chuudoku-girl.json) | BPM、音高范围 |
| [ラストラス](../data/songs/lustrous.json) | 音高范围 |
| [キャットフード](../data/songs/cat-food.json) | 音高范围 |
| [月光潤色ガール](../data/songs/gekkou-junshoku-girl.json) | 音高范围 |
| [少女ケシゴム](../data/songs/shoujo-keshigomu.json) | BPM、音高范围 |
| [1/6 -out of the gravity-](../data/songs/1-6-out-of-the-gravity.json) | 音高范围 |
| [夏に去りし君を想フ](../data/songs/natsu-ni-sarishi-kimi-o-omou.json) | 音高范围 |
| [むかしむかしのきょうのぼく](../data/songs/mukashi-mukashi-no-kyou-no-boku.json) | 音高范围 |
| [自傷無色](../data/songs/jishou-mushoku.json) | 音高范围 |
| [she](../data/songs/she.json) | BPM、音高范围 |
| [新人類](../data/songs/shinjinrui.json) | 音高范围 |
| [ブレス・ユア・ブレス](../data/songs/bless-your-breath.json) | 音高范围 |
| [セカイ](../data/songs/sekai.json) | 音高范围 |
| [東京レトロ](../data/songs/tokyo-retro.json) | 音高范围 |
| [SnowMix♪](../data/songs/snowmix.json) | 音高范围 |
| [エンパープル](../data/songs/empurple.json) | 音高范围 |
| [四角い地球を丸くする](../data/songs/shikakui-chikyuu-o-maruku-suru.json) | 音高范围 |
| [勘違い性反希望症](../data/songs/kanchigai-seihan-kiboushou.json) | BPM、音高范围 |
| [Blue Star](../data/songs/blue-star.json) | BPM、音高范围 |
| [8.39](../data/songs/vocadb-252103.json) | BPM、音高范围 |
| [繰り返し一粒](../data/songs/kurikaeshi-hitotsubu.json) | BPM、音高范围 |
| [モア！ジャンプ！モア！](../data/songs/more-jump-more.json) | 音高范围 |
| [Starduster](../data/songs/starduster.json) | 音高范围 |
| [こちら、幸福安心委員会です。](../data/songs/kochira-koufuku-anshin-iinkai-desu.json) | 音高范围 |
| [幸せになれる隠しコマンドがあるらしい](../data/songs/shiawase-ni-nareru-kakushi-command-ga-arurashii.json) | 音高范围 |
| [恋の恋による恋のための恋](../data/songs/koi-no-koi-ni-yoru-koi-no-tame-no-koi.json) | 音高范围 |
| [好き！雪！本気マジック](../data/songs/suki-yuki-maji-magic.json) | 音高范围 |
| [嗚咽](../data/songs/oetsu.json) | BPM、音高范围 |
| [文学者の恋文](../data/songs/bungakusha-no-koibumi.json) | 音高范围 |
| [虹色蝶々](../data/songs/nijiiro-chouchou.json) | BPM、音高范围 |
| [僕が夢を捨てて大人になるまで](../data/songs/boku-ga-yume-o-sutete-otona-ni-naru-made.json) | BPM、音高范围 |
| [心予報](../data/songs/kokoro-yohou.json) | 音高范围 |
| [ブループラネット](../data/songs/blue-planet.json) | 音高范围 |
| [夜に駆ける](../data/songs/yoru-ni-kakeru.json) | 音高范围 |
| [針鼠](../data/songs/harinezumi.json) | BPM、音高范围 |
| [ラストスコア](../data/songs/last-score.json) | 音高范围 |
| [DECORATOR](../data/songs/decorator.json) | 音高范围 |
| [夕日坂](../data/songs/yuuhizaka.json) | 音高范围 |
| [White Landscape](../data/songs/white-landscape.json) | BPM、音高范围 |
| [八十八鍵の宇宙](../data/songs/hachi-juu-hachi-ken-no-uchuu.json) | 音高范围 |
| [心象蜃気楼](../data/songs/shinshou-shinkirou.json) | 音高范围 |
| [酔いどれ知らず](../data/songs/yoidore-shirazu.json) | 音高范围 |
| [サイエンス](../data/songs/science.json) | 音高范围 |
| [明正ロマン](../data/songs/meishou-romance.json) | 音高范围 |
| [おべか](../data/songs/obeka.json) | BPM、音高范围 |
| [ウルトラトレーラー](../data/songs/ultra-trailer.json) | 音高范围 |
| [ちっちゃな私](../data/songs/chiccha-na-watashi.json) | 音高范围 |
| [いいねってYEAH!](../data/songs/ii-ne-tte-yeah.json) | BPM、音高范围 |
| [少女人形の見た夢](../data/songs/shoujo-ningyou-no-mita-yume.json) | 音高范围 |
| [ニヒルと水没都市](../data/songs/nihil-to-suibotsu-toshi.json) | BPM、音高范围 |
| [表裏一体](../data/songs/hyouri-ittai.json) | 音高范围 |
| [アマツキツネ](../data/songs/amatsu-kitsune.json) | 音高范围 |
| [怪盗・窪園チヨコは絶対ミスらない](../data/songs/kaitou-kubozono-chiyoko-wa-zettai-misuranai.json) | 音高范围 |
| [モザイクロール](../data/songs/mozaik-role.json) | 音高范围 |
| [マネマネサイコトロピック](../data/songs/mane-mane-psychotropic.json) | 音高范围 |
| [あしゅらしゅら](../data/songs/ashura-shura.json) | 音高范围 |
| [熱異常](../data/songs/netsu-ijou.json) | 音高范围 |

## 音高来源冲突：保留空白

同一标题的参考站点出现下列不同范围，未擅自合并或择一。不同版本或纳入和声/装饰音可能是差异原因。这里的值是来源所载的候选值，不是歌曲的已确认音域。

| 歌曲 | 来源所载的不同范围 |
| --- | --- |
| [エイリアンエイリアン](../data/songs/alien-alien.json) | [B3～C6](https://entertainment-holic.com/range-of-vocaloid-popular-songs/3/)；[D4～C6](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [パンダヒーロー](../data/songs/panda-hero.json) | [B3～B5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/)；[A3～B5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [ローリンガール](../data/songs/rollin-girl.json) | [C#4～B5](https://entertainment-holic.com/range-of-rollin-girl-composed-by-wowaka/)；[D4～B5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [フォニイ](../data/songs/phony.json) | [G3～G#5](https://entertainment-holic.com/range-of-phony-composed-by-tsumiki/)；[A3～G#5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [アンドロイドガール](../data/songs/android-girl.json) | [E4～F#5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/2/)；[E3～F#5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [夜明けと蛍](../data/songs/yoake-to-hotaru.json) | [G3～G#5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/2/)；[F#3～G#5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [シンデレラ](../data/songs/cinderella.json) | [A#3～A#5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/2/)；[F4～A#5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [ダーリンダンス](../data/songs/darling-dance.json) | [A3～C6](https://entertainment-holic.com/range-of-vocaloid-popular-songs/)；[F#4～C6](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [神っぽいな](../data/songs/kamippoi-na.json) | [A3～D#6](https://entertainment-holic.com/range-of-kamippoina-composed-by-pinocchiop/)；[F4～D#6](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [カレシのジュード](../data/songs/kareshi-no-jude.json) | [A3～D6](https://entertainment-holic.com/range-of-vocaloid-popular-songs/2/)；[F#4～D6](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [ジャンキーナイトタウンオーケストラ](../data/songs/junky-night-town-orchestra.json) | [D#4～G5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/2/)；[D#4～A#5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [メンタルチェンソー](../data/songs/mental-chainsaw.json) | [A#3～F5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/2/)；[D4～F5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [p.h.](../data/songs/p-h.json) | [D3～A#4](https://entertainment-holic.com/range-of-vocaloid-popular-songs/3/)；[D4～A#5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [魔法少女とチョコレゐト](../data/songs/mahou-shoujo-to-chocolate.json) | [C#4～F#5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/)；[C#4～F5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [きゅうくらりん](../data/songs/kyuukurarin.json) | [G#3～G#5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/)；[B3～F5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [ECHO](../data/songs/echo.json) | [F#3～G#5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/)；[C#4～F#5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html)；[F#3～G#5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [シャンティ](../data/songs/shanti.json) | [C3～F4](https://entertainment-holic.com/range-of-vocaloid-popular-songs/3/)；[C#3～F#4](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [人マニア](../data/songs/hito-mania.json) | [C#4～D#5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/)；[D#4～D#5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [キライ・キライ・ジガヒダイ！](../data/songs/kirai-kirai-jiga-hidai.json) | [A3～E5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/2/)；[A3～G5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [Bad ∞ End ∞ Night](../data/songs/bad-end-night.json) | [A2～C6](https://entertainment-holic.com/range-of-vocaloid-popular-songs/2/)；[A2～C#6](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [愛言葉Ⅲ](../data/songs/ai-kotoba-iii.json) | [G3～E5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/3/)；[G#3～E5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [ホワイトハッピー](../data/songs/white-happy.json) | [A#3～F#5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/2/)；[C4～F#5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [帝国少女](../data/songs/teikoku-shoujo.json) | [B3～F#5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/)；[B3～E5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [ド屑](../data/songs/dokuzu.json) | [F#3～D#5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/2/)；[F#3～F5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [39](../data/songs/vocadb-14480.json) | [F3～F5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/)；[B3～G5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [Blessing](../data/songs/blessing.json) | [G3～F#5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/3/)；[D3～F#5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [こちら、幸福安心委員会です。](../data/songs/kochira-koufuku-anshin-iinkai-desu.json) | [A3～C5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/3/)；[B3～G#4](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [好き！雪！本気マジック](../data/songs/suki-yuki-maji-magic.json) | [B3～E5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/4/)；[D4～E5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [酔いどれ知らず](../data/songs/yoidore-shirazu.json) | [A3～D5](https://entertainment-holic.com/range-of-yoidore-shirazu-composed-by-kanaria/)；[A3～E5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [モザイクロール](../data/songs/mozaik-role.json) | [B3～D5](https://entertainment-holic.com/range-of-vocaloid-popular-songs/4/)；[B3～D#5](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |
| [熱異常](../data/songs/netsu-ijou.json) | [G#3～G#6](https://entertainment-holic.com/range-of-heat-abnormal-composed-by-iyowa/)；[A#2～G#6](https://w.atwiki.jp/saikouon_dokoda/pages/472.html) |

## 全部新增歌曲与元数据来源

| 歌曲 | 元数据 |
| --- | --- |
| [ルカルカ★ナイトフィーバー](../data/songs/luka-lukanight-fever.json) | [VocaDB](https://vocadb.net/S/1435) |
| [エイリアンエイリアン](../data/songs/alien-alien.json) | [VocaDB](https://vocadb.net/S/106773) |
| [砂の惑星](../data/songs/suna-no-wakusei.json) | [VocaDB](https://vocadb.net/S/157860) |
| [ハロ／ハワユ](../data/songs/hello-how-are-you.json) | [VocaDB](https://vocadb.net/S/1416) |
| [ヒバナ](../data/songs/hibana.json) | [VocaDB](https://vocadb.net/S/164074) |
| [グッバイ宣言](../data/songs/goodbye-sengen.json) | [VocaDB](https://vocadb.net/S/278267) |
| [ベノム](../data/songs/venom.json) | [VocaDB](https://vocadb.net/S/199209) |
| [吉原ラメント](../data/songs/yoshiwara-lament.json) | [VocaDB](https://vocadb.net/S/14435) |
| [命に嫌われている。](../data/songs/inochi-ni-kirawarete-iru.json) | [VocaDB](https://vocadb.net/S/164273) |
| [アスノヨゾラ哨戒班](../data/songs/asu-no-yozora-shoukaihan.json) | [VocaDB](https://vocadb.net/S/65861) |
| [みくみくにしてあげる♪【してやんよ】](../data/songs/miku-miku-ni-shite-ageru-shite-yan-yo.json) | [VocaDB](https://vocadb.net/S/1355) |
| [テレキャスタービーボーイ](../data/songs/telecaster-b-boy.json) | [VocaDB](https://vocadb.net/S/233017) |
| [パンダヒーロー](../data/songs/panda-hero.json) | [VocaDB](https://vocadb.net/S/2978) |
| [気まぐれメルシィ](../data/songs/kimagure-mercy.json) | [VocaDB](https://vocadb.net/S/121935) |
| [from Y to Y](../data/songs/from-y-to-y.json) | [VocaDB](https://vocadb.net/S/4230) |
| [心做し](../data/songs/kokoronashi.json) | [VocaDB](https://vocadb.net/S/46115) |
| [ヴァンパイア](../data/songs/vampire.json) | [VocaDB](https://vocadb.net/S/321205) |
| [ロストワンの号哭](../data/songs/lost-one-no-goukoku.json) | [VocaDB](https://vocadb.net/S/19094) |
| [東京テディベア](../data/songs/tokyo-teddy-bear.json) | [VocaDB](https://vocadb.net/S/555) |
| [夜咄ディセイブ](../data/songs/yobanashi-deceive.json) | [VocaDB](https://vocadb.net/S/23087) |
| [独りんぼエンヴィー](../data/songs/hitorinbo-envy.json) | [VocaDB](https://vocadb.net/S/18479) |
| [ゴーストルール](../data/songs/ghost-rule.json) | [VocaDB](https://vocadb.net/S/112085) |
| [東京サマーセッション](../data/songs/tokyo-summer-session.json) | [VocaDB](https://vocadb.net/S/96106) |
| [幽霊東京](../data/songs/yuurei-tokyo.json) | [VocaDB](https://vocadb.net/S/262740) |
| [Just Be Friends](../data/songs/just-be-friends.json) | [VocaDB](https://vocadb.net/S/1360) |
| [＊ハロー、プラネット。](../data/songs/hello-planet.json) | [VocaDB](https://vocadb.net/S/2924) |
| [神のまにまに](../data/songs/kami-no-manimani.json) | [VocaDB](https://vocadb.net/S/47759) |
| [ワールズエンド・ダンスホール](../data/songs/world-s-end-dancehall.json) | [VocaDB](https://vocadb.net/S/20) |
| [サマータイムレコード](../data/songs/summertime-record.json) | [VocaDB](https://vocadb.net/S/28648) |
| [ロミオとシンデレラ](../data/songs/romeo-to-cinderella.json) | [VocaDB](https://vocadb.net/S/1032) |
| [セツナトリップ](../data/songs/setsuna-trip.json) | [VocaDB](https://vocadb.net/S/11807) |
| [ワールドイズマイン](../data/songs/world-is-mine.json) | [VocaDB](https://vocadb.net/S/1326) |
| [ビターチョコデコレーション](../data/songs/bitter-choco-decoration.json) | [VocaDB](https://vocadb.net/S/221277) |
| [炉心融解](../data/songs/roshin-yuukai.json) | [VocaDB](https://vocadb.net/S/3022) |
| [妄想感傷代償連盟](../data/songs/mousou-kanshou-daishou-renmei.json) | [VocaDB](https://vocadb.net/S/131090) |
| [ブラック★ロックシューター](../data/songs/blackrock-shooter.json) | [VocaDB](https://vocadb.net/S/1323) |
| [ドラマツルギー](../data/songs/dramaturgy.json) | [VocaDB](https://vocadb.net/S/170110) |
| [惑星ループ](../data/songs/wakusei-loop.json) | [VocaDB](https://vocadb.net/S/137609) |
| [妄想税](../data/songs/mousouzei.json) | [VocaDB](https://vocadb.net/S/38916) |
| [ロスタイムメモリー](../data/songs/lost-time-memory.json) | [VocaDB](https://vocadb.net/S/25896) |
| [劣等上等](../data/songs/rettou-joutou.json) | [VocaDB](https://vocadb.net/S/192291) |
| [チュルリラ・チュルリラ・ダッダッダ！](../data/songs/chururira-chururira-daddadda.json) | [VocaDB](https://vocadb.net/S/115476) |
| [だれかの心臓になれたなら](../data/songs/dareka-no-shinzou-ni-nareta-nara.json) | [VocaDB](https://vocadb.net/S/184133) |
| [Dear](../data/songs/dear.json) | [VocaDB](https://vocadb.net/S/3478) |
| [オレンジ](../data/songs/orange.json) | [VocaDB](https://vocadb.net/S/19058) |
| [地球最後の告白を](../data/songs/chikyuu-saigo-no-kokuhaku-o.json) | [VocaDB](https://vocadb.net/S/13615) |
| [空想フォレスト](../data/songs/kuusou-forest.json) | [VocaDB](https://vocadb.net/S/46886) |
| [ローリンガール](../data/songs/rollin-girl.json) | [VocaDB](https://vocadb.net/S/1501) |
| [フォニイ](../data/songs/phony.json) | [VocaDB](https://vocadb.net/S/337578) |
| [アンドロイドガール](../data/songs/android-girl.json) | [VocaDB](https://vocadb.net/S/230406) |
| [テオ](../data/songs/teo.json) | [VocaDB](https://vocadb.net/S/161199) |
| [コールボーイ](../data/songs/call-boy.json) | [VocaDB](https://vocadb.net/S/231791) |
| [右肩の蝶](../data/songs/migikata-no-chou.json) | [VocaDB](https://vocadb.net/S/1952) |
| [ハッピーシンセサイザ](../data/songs/happy-synthesizer.json) | [VocaDB](https://vocadb.net/S/3177) |
| [いーあるふぁんくらぶ](../data/songs/yi-er-fanclub.json) | [VocaDB](https://vocadb.net/S/15785) |
| [人生リセットボタン](../data/songs/jinsei-reset-button.json) | [VocaDB](https://vocadb.net/S/8250) |
| [ナンセンス文学](../data/songs/nonsense-bungaku.json) | [VocaDB](https://vocadb.net/S/157227) |
| [チルドレンレコード](../data/songs/children-record.json) | [VocaDB](https://vocadb.net/S/14484) |
| [DAYBREAK FRONTLINE](../data/songs/daybreak-frontline.json) | [VocaDB](https://vocadb.net/S/141339) |
| [rain stops, good-bye](../data/songs/rain-stops-good-bye.json) | [VocaDB](https://vocadb.net/S/8521) |
| [夜明けと蛍](../data/songs/yoake-to-hotaru.json) | [VocaDB](https://vocadb.net/S/71884) |
| [magnet](../data/songs/magnet.json) | [VocaDB](https://vocadb.net/S/5166) |
| [天樂](../data/songs/tengaku.json) | [VocaDB](https://vocadb.net/S/3269) |
| [バレリーコ](../data/songs/balleriko.json) | [VocaDB](https://vocadb.net/S/62650) |
| [シンデレラ](../data/songs/cinderella.json) | [VocaDB](https://vocadb.net/S/346457) |
| [ダーリンダンス](../data/songs/darling-dance.json) | [VocaDB](https://vocadb.net/S/293286) |
| [キュートなカノジョ](../data/songs/cute-na-kanojo.json) | [VocaDB](https://vocadb.net/S/316298) |
| [エゴロック](../data/songs/ego-rock.json) | [VocaDB](https://vocadb.net/S/202936) |
| [深海少女](../data/songs/shinkai-shoujo.json) | [VocaDB](https://vocadb.net/S/8735) |
| [ウミユリ海底譚](../data/songs/umiyuri-kaitei-tan.json) | [VocaDB](https://vocadb.net/S/49871) |
| [夜撫でるメノウ](../data/songs/yoru-naderu-menou.json) | [VocaDB](https://vocadb.net/S/225817) |
| [回る空うさぎ](../data/songs/mawaru-sora-usagi.json) | [VocaDB](https://vocadb.net/S/139902) |
| [少女レイ](../data/songs/shoujo-rei.json) | [VocaDB](https://vocadb.net/S/197929) |
| [告白ライバル宣言](../data/songs/kokuhaku-rival-sengen.json) | [VocaDB](https://vocadb.net/S/48083) |
| [夜もすがら君想ふ](../data/songs/yomosugara-kimi-omou.json) | [VocaDB](https://vocadb.net/S/51262) |
| [二息歩行](../data/songs/nisoku-hokou.json) | [VocaDB](https://vocadb.net/S/5859) |
| [Calc.](../data/songs/calc.json) | [VocaDB](https://vocadb.net/S/7801) |
| [ジャックポットサッドガール](../data/songs/jack-pot-sad-girl.json) | [VocaDB](https://vocadb.net/S/299484) |
| [え？あぁ、そう。](../data/songs/e-aa-sou.json) | [VocaDB](https://vocadb.net/S/2716) |
| [神っぽいな](../data/songs/kamippoi-na.json) | [VocaDB](https://vocadb.net/S/354245) |
| [パラジクロロベンゼン](../data/songs/paradichlorobenzene.json) | [VocaDB](https://vocadb.net/S/1890) |
| [生きる](../data/songs/ikiru.json) | [VocaDB](https://vocadb.net/S/344714) |
| [悪ノ娘](../data/songs/aku-no-musume.json) | [VocaDB](https://vocadb.net/S/1590) |
| [シネマ](../data/songs/cinema.json) | [VocaDB](https://vocadb.net/S/333025) |
| [ヒビカセ](../data/songs/hibikase.json) | [VocaDB](https://vocadb.net/S/63276) |
| [裏表ラバーズ](../data/songs/uraomote-lovers.json) | [VocaDB](https://vocadb.net/S/1508) |
| [太陽系デスコ](../data/songs/taiyoukei-disco.json) | [VocaDB](https://vocadb.net/S/129109) |
| [ルマ](../data/songs/ruma.json) | [VocaDB](https://vocadb.net/S/261802) |
| [カレシのジュード](../data/songs/kareshi-no-jude.json) | [VocaDB](https://vocadb.net/S/347355) |
| [パメラ](../data/songs/pamela.json) | [VocaDB](https://vocadb.net/S/359877) |
| [SPiCa](../data/songs/spica.json) | [VocaDB](https://vocadb.net/S/1516) |
| [初めての恋が終わる時](../data/songs/hajimete-no-koi-ga-owaru-toki.json) | [VocaDB](https://vocadb.net/S/1327) |
| [敗北の少年](../data/songs/haiboku-no-shounen.json) | [VocaDB](https://vocadb.net/S/12139) |
| [快晴](../data/songs/kaisei.json) | [VocaDB](https://vocadb.net/S/166707) |
| [アニマル](../data/songs/animal.json) | [VocaDB](https://vocadb.net/S/371426) |
| [カミサマネジマキ](../data/songs/kamisama-nejimaki.json) | [VocaDB](https://vocadb.net/S/12136) |
| [脱法ロック](../data/songs/dappou-rock.json) | [VocaDB](https://vocadb.net/S/127169) |
| [ラストリゾート](../data/songs/last-resort.json) | [VocaDB](https://vocadb.net/S/236272) |
| [トンデモワンダーズ](../data/songs/tondemo-wonderz.json) | [VocaDB](https://vocadb.net/S/340035) |
| [林檎売りの泡沫少女](../data/songs/ringo-uri-no-utakata-shoujo.json) | [VocaDB](https://vocadb.net/S/12657) |
| [ツギハギスタッカート](../data/songs/tsugihagi-staccato.json) | [VocaDB](https://vocadb.net/S/58632) |
| [サリシノハラ](../data/songs/sarishi-no-hara.json) | [VocaDB](https://vocadb.net/S/16783) |
| [お気に召すまま](../data/songs/oki-ni-mesu-mama.json) | [VocaDB](https://vocadb.net/S/175905) |
| [Henceforth](../data/songs/henceforth.json) | [VocaDB](https://vocadb.net/S/282574) |
| [カラフル×メロディ](../data/songs/colorfulmelody.json) | [VocaDB](https://vocadb.net/S/2920) |
| [ジャンキーナイトタウンオーケストラ](../data/songs/junky-night-town-orchestra.json) | [VocaDB](https://vocadb.net/S/265022) |
| [ラヴィット](../data/songs/loveit.json) | [VocaDB](https://vocadb.net/S/298528) |
| [ぼくらの16bit戦争](../data/songs/bokura-no-16bit-wars.json) | [VocaDB](https://vocadb.net/S/5244) |
| [再教育](../data/songs/saikyouiku.json) | [VocaDB](https://vocadb.net/S/13728) |
| [FREELY TOMORROW](../data/songs/freely-tomorrow.json) | [VocaDB](https://vocadb.net/S/5364) |
| [阿吽のビーツ](../data/songs/aun-no-beats.json) | [VocaDB](https://vocadb.net/S/165658) |
| [アンノウン・マザーグース](../data/songs/unknown-mother-goose.json) | [VocaDB](https://vocadb.net/S/164107) |
| [ダンスロボットダンス](../data/songs/dance-robot-dance.json) | [VocaDB](https://vocadb.net/S/141649) |
| [メンタルチェンソー](../data/songs/mental-chainsaw.json) | [VocaDB](https://vocadb.net/S/325636) |
| [恋は戦争](../data/songs/koi-wa-sensou.json) | [VocaDB](https://vocadb.net/S/1320) |
| [エンヴィキャットウォーク](../data/songs/envy-catwalk.json) | [VocaDB](https://vocadb.net/S/453) |
| [雨とペトラ](../data/songs/ame-to-petra.json) | [VocaDB](https://vocadb.net/S/150978) |
| [インビジブル](../data/songs/invisible.json) | [VocaDB](https://vocadb.net/S/8251) |
| [アイロニ](../data/songs/irony.json) | [VocaDB](https://vocadb.net/S/12476) |
| [リンネ](../data/songs/rinne.json) | [VocaDB](https://vocadb.net/S/2980) |
| [EYE](../data/songs/eye.json) | [VocaDB](https://vocadb.net/S/345108) |
| [p.h.](../data/songs/p-h.json) | [VocaDB](https://vocadb.net/S/278776) |
| [魔法少女とチョコレゐト](../data/songs/mahou-shoujo-to-chocolate.json) | [VocaDB](https://vocadb.net/S/387848) |
| [告白予行練習](../data/songs/kokuhaku-yokou-renshuu.json) | [VocaDB](https://vocadb.net/S/17514) |
| [マーシャル・マキシマイザー](../data/songs/marshall-maximizer.json) | [VocaDB](https://vocadb.net/S/348255) |
| [おちゃめ機能](../data/songs/ochame-kinou.json) | [VocaDB](https://vocadb.net/S/4176) |
| [ODDS&ENDS](../data/songs/odds-ends.json) | [VocaDB](https://vocadb.net/S/15662) |
| [それがあなたの幸せとしても](../data/songs/sore-ga-anata-no-shiawase-to-shite-mo.json) | [VocaDB](https://vocadb.net/S/26010) |
| [ピエロ](../data/songs/pierrot.json) | [VocaDB](https://vocadb.net/S/3872) |
| [キャットラビング](../data/songs/cat-loving.json) | [VocaDB](https://vocadb.net/S/344094) |
| [愛して愛して愛して](../data/songs/aishite-aishite-aishite.json) | [VocaDB](https://vocadb.net/S/25667) |
| [キメラ](../data/songs/chimera.json) | [VocaDB](https://vocadb.net/S/396081) |
| [ダンシング☆サムライ](../data/songs/dancingsamurai.json) | [VocaDB](https://vocadb.net/S/1275) |
| [如月アテンション](../data/songs/kisaragi-attention.json) | [VocaDB](https://vocadb.net/S/12518) |
| [Fire◎Flower](../data/songs/fireflower.json) | [VocaDB](https://vocadb.net/S/6387) |
| [アイデンティティ](../data/songs/identity.json) | [VocaDB](https://vocadb.net/S/377317) |
| [結ンデ開イテ羅刹ト骸](../data/songs/musunde-hiraite-rasetsu-to-mukuro.json) | [VocaDB](https://vocadb.net/S/2982) |
| [臨界ダイバー](../data/songs/rinkai-diver.json) | [VocaDB](https://vocadb.net/S/146648) |
| [サンドリヨン](../data/songs/cendrillon.json) | [VocaDB](https://vocadb.net/S/7238) |
| [爆笑](../data/songs/bakushou.json) | [VocaDB](https://vocadb.net/S/336190) |
| [ノンブレス・オブリージュ](../data/songs/non-breath-oblige.json) | [VocaDB](https://vocadb.net/S/335988) |
| [きゅうくらりん](../data/songs/kyuukurarin.json) | [VocaDB](https://vocadb.net/S/349763) |
| [白い雪のプリンセスは](../data/songs/shiroi-yuki-no-princess-wa.json) | [VocaDB](https://vocadb.net/S/3312) |
| [チェチェ・チェック・ワンツー！](../data/songs/check-check-check-one-two.json) | [VocaDB](https://vocadb.net/S/129113) |
| [春嵐](../data/songs/shunran.json) | [VocaDB](https://vocadb.net/S/263327) |
| [ロストアンブレラ](../data/songs/lost-umbrella.json) | [VocaDB](https://vocadb.net/S/185364) |
| [いかないで](../data/songs/ikanaide.json) | [VocaDB](https://vocadb.net/S/41593) |
| [夕景イエスタデイ](../data/songs/yuukei-yesterday.json) | [VocaDB](https://vocadb.net/S/25898) |
| [ココロ](../data/songs/kokoro.json) | [VocaDB](https://vocadb.net/S/1357) |
| [バグ](../data/songs/bug.json) | [VocaDB](https://vocadb.net/S/416174) |
| [透明エレジー](../data/songs/toumei-elegy.json) | [VocaDB](https://vocadb.net/S/23473) |
| [ECHO](../data/songs/echo.json) | [VocaDB](https://vocadb.net/S/68814) |
| [QUEEN](../data/songs/queen.json) | [VocaDB](https://vocadb.net/S/429733) |
| [絶対敵対メチャキライヤー](../data/songs/zettai-tekitai-mecha-kirai-yaa.json) | [VocaDB](https://vocadb.net/S/401500) |
| [ヤンキーボーイ・ヤンキーガール](../data/songs/yankee-boy-yankee-girl.json) | [VocaDB](https://vocadb.net/S/21210) |
| [ロウワー](../data/songs/lower.json) | [VocaDB](https://vocadb.net/S/365108) |
| [ライアーダンス](../data/songs/liar-dance.json) | [VocaDB](https://vocadb.net/S/125735) |
| [トゥインクル](../data/songs/twinkle.json) | [VocaDB](https://vocadb.net/S/5361) |
| [shake it！](../data/songs/shake-it.json) | [VocaDB](https://vocadb.net/S/11593) |
| [ハウトゥー世界征服](../data/songs/how-to-sekai-seifuku.json) | [VocaDB](https://vocadb.net/S/22539) |
| [アンハッピーリフレイン](../data/songs/unhappy-refrain.json) | [VocaDB](https://vocadb.net/S/1500) |
| [エバ](../data/songs/eva.json) | [VocaDB](https://vocadb.net/S/266933) |
| [聖槍爆裂ボーイ](../data/songs/seisou-bakuretsu-boy.json) | [VocaDB](https://vocadb.net/S/38393) |
| [ラビットホール](../data/songs/rabbit-hole.json) | [VocaDB](https://vocadb.net/S/500519) |
| [シャンティ](../data/songs/shanti.json) | [VocaDB](https://vocadb.net/S/354249) |
| [腐れ外道とチョコレゐト](../data/songs/kusaregedou-to-chocolate.json) | [VocaDB](https://vocadb.net/S/136) |
| [ケッペキショウ](../data/songs/keppeki-shou.json) | [VocaDB](https://vocadb.net/S/18917) |
| [-ERROR](../data/songs/error.json) | [VocaDB](https://vocadb.net/S/13339) |
| [メリュー](../data/songs/meru.json) | [VocaDB](https://vocadb.net/S/87458) |
| [金曜日のおはよう-another story-](../data/songs/kinyoubi-no-ohayou-another-story.json) | [VocaDB](https://vocadb.net/S/68296) |
| [ねぇねぇねぇ。](../data/songs/nee-nee-nee.json) | [VocaDB](https://vocadb.net/S/335986) |
| [君はできない子](../data/songs/kimi-wa-dekinai-ko.json) | [VocaDB](https://vocadb.net/S/25725) |
| [十面相](../data/songs/juumensou.json) | [VocaDB](https://vocadb.net/S/133) |
| [命ばっかり](../data/songs/inochi-bakkari.json) | [VocaDB](https://vocadb.net/S/164101) |
| [人マニア](../data/songs/hito-mania.json) | [VocaDB](https://vocadb.net/S/520007) |
| [ラグトレイン](../data/songs/lagtrain.json) | [VocaDB](https://vocadb.net/S/288238) |
| [悪魔の踊り方](../data/songs/akuma-no-odorikata.json) | [VocaDB](https://vocadb.net/S/191674) |
| [IMAWANOKIWA](../data/songs/imawanokiwa.json) | [VocaDB](https://vocadb.net/S/259741) |
| [テトリス](../data/songs/tetoris.json) | [VocaDB](https://vocadb.net/S/696221) |
| [リモコン](../data/songs/remocon.json) | [VocaDB](https://vocadb.net/S/3387) |
| [ペテン師が笑う頃に](../data/songs/petenshi-ga-warau-koro-ni.json) | [VocaDB](https://vocadb.net/S/1125) |
| [キライ・キライ・ジガヒダイ！](../data/songs/kirai-kirai-jiga-hidai.json) | [VocaDB](https://vocadb.net/S/129549) |
| [モニタリング](../data/songs/monitoring.json) | [VocaDB](https://vocadb.net/S/668055) |
| [骸骨楽団とリリア](../data/songs/gaikotsu-gakudan-to-lilia.json) | [VocaDB](https://vocadb.net/S/556) |
| [混沌ブギ](../data/songs/konton-boogie.json) | [VocaDB](https://vocadb.net/S/525760) |
| [オーバーライド](../data/songs/override.json) | [VocaDB](https://vocadb.net/S/557307) |
| [上弦の月](../data/songs/jougen-no-tsuki.json) | [VocaDB](https://vocadb.net/S/22869) |
| [いろは唄](../data/songs/iroha-uta.json) | [VocaDB](https://vocadb.net/S/2738) |
| [テレパシ](../data/songs/telepathy.json) | [VocaDB](https://vocadb.net/S/752940) |
| [IMITATION BLACK](../data/songs/imitation-black.json) | [VocaDB](https://vocadb.net/S/1250) |
| [花弁、それにまつわる音声](../data/songs/kaben-sore-ni-matsuwaru-onsei.json) | [VocaDB](https://vocadb.net/S/753297) |
| [Bad ∞ End ∞ Night](../data/songs/bad-end-night.json) | [VocaDB](https://vocadb.net/S/8682) |
| [オツキミリサイタル](../data/songs/otsukimi-recital.json) | [VocaDB](https://vocadb.net/S/25901) |
| [おこちゃま戦争](../data/songs/okochama-sensou.json) | [VocaDB](https://vocadb.net/S/44190) |
| [Leia - Remind](../data/songs/leia-remind.json) | [VocaDB](https://vocadb.net/S/210407) |
| [虎視眈々](../data/songs/koshitantan.json) | [VocaDB](https://vocadb.net/S/42554) |
| [88☆彡](../data/songs/vocadb-400359.json) | [VocaDB](https://vocadb.net/S/400359) |
| [あの夏のいつかは](../data/songs/ano-natsu-no-itsuka-wa.json) | [VocaDB](https://vocadb.net/S/248234) |
| [朧月](../data/songs/oborodzuki.json) | [VocaDB](https://vocadb.net/S/5172) |
| [内臓ありますか](../data/songs/naizou-arimasu-ka.json) | [VocaDB](https://vocadb.net/S/219729) |
| [愛言葉](../data/songs/ai-kotoba.json) | [VocaDB](https://vocadb.net/S/3019) |
| [愛言葉Ⅱ](../data/songs/ai-kotoba-ii.json) | [VocaDB](https://vocadb.net/S/41545) |
| [愛言葉Ⅲ](../data/songs/ai-kotoba-iii.json) | [VocaDB](https://vocadb.net/S/207153) |
| [愛言葉Ⅳ](../data/songs/ai-kotoba-iv.json) | [VocaDB](https://vocadb.net/S/409527) |
| [愛言葉Ⅴ](../data/songs/ai-kotoba-v.json) | [VocaDB](https://vocadb.net/S/915394) |
| [千本桜](../data/songs/senbonzakura.json) | [VocaDB](https://vocadb.net/S/8394) |
| [白ゆき](../data/songs/shirayuki.json) | [VocaDB](https://vocadb.net/S/119843) |
| [paranoia](../data/songs/paranoia.json) | [VocaDB](https://vocadb.net/S/10018) |
| [ホワイトハッピー](../data/songs/white-happy.json) | [VocaDB](https://vocadb.net/S/160508) |
| [僕は初音ミクとキスをした](../data/songs/boku-wa-hatsune-miku-to-kiss-o-shita.json) | [VocaDB](https://vocadb.net/S/26013) |
| [ハローセカイ](../data/songs/hello-sekai.json) | [VocaDB](https://vocadb.net/S/730826) |
| [脱獄](../data/songs/datsugoku.json) | [VocaDB](https://vocadb.net/S/97727) |
| [アカツキアライヴァル](../data/songs/akatsuki-arrival.json) | [VocaDB](https://vocadb.net/S/9553) |
| [夢と葉桜](../data/songs/yume-to-hazakura.json) | [VocaDB](https://vocadb.net/S/5362) |
| [だんだん早くなる](../data/songs/dandan-hayaku-naru.json) | [VocaDB](https://vocadb.net/S/81641) |
| [アンヘル](../data/songs/angel.json) | [VocaDB](https://vocadb.net/S/231284) |
| [ザムザ](../data/songs/samsa.json) | [VocaDB](https://vocadb.net/S/490444) |
| [星屑ユートピア](../data/songs/hoshikuzu-utopia.json) | [VocaDB](https://vocadb.net/S/1047) |
| [番凩](../data/songs/tsugai-kogarashi.json) | [VocaDB](https://vocadb.net/S/8241) |
| [世界寿命と最後の一日](../data/songs/sekai-jumyou-to-saigo-no-ichinichi.json) | [VocaDB](https://vocadb.net/S/38789) |
| [Black Board](../data/songs/black-board.json) | [VocaDB](https://vocadb.net/S/10580) |
| [祝福のメシアとアイの塔](../data/songs/shukufuku-no-messiah-to-ai-no-tou.json) | [VocaDB](https://vocadb.net/S/129187) |
| [インタビュア](../data/songs/interviewer.json) | [VocaDB](https://vocadb.net/S/9538) |
| [花降らし](../data/songs/hana-furashi.json) | [VocaDB](https://vocadb.net/S/124846) |
| [心拍数♯0822](../data/songs/shinpakusuu-0822.json) | [VocaDB](https://vocadb.net/S/6099) |
| [letter song](../data/songs/letter-song.json) | [VocaDB](https://vocadb.net/S/1077) |
| [日常と地球の額縁](../data/songs/nichijou-to-chikyuu-no-gakubuchi.json) | [VocaDB](https://vocadb.net/S/1504) |
| [君恋し](../data/songs/kimi-koishi.json) | [VocaDB](https://vocadb.net/S/3183) |
| [パズル](../data/songs/puzzle.json) | [VocaDB](https://vocadb.net/S/1319) |
| [四季折の羽](../data/songs/shikiori-no-hane.json) | [VocaDB](https://vocadb.net/S/35874) |
| [レッド・パージ！！！](../data/songs/red-purge.json) | [VocaDB](https://vocadb.net/S/47771) |
| [蜘蛛糸モノポリー](../data/songs/kumo-ito-monopoly.json) | [VocaDB](https://vocadb.net/S/18371) |
| [帝国少女](../data/songs/teikoku-shoujo.json) | [VocaDB](https://vocadb.net/S/150952) |
| [カンタレラ](../data/songs/cantarella.json) | [VocaDB](https://vocadb.net/S/3021) |
| [ドリームレス・ドリームス](../data/songs/dreamless-dreams.json) | [VocaDB](https://vocadb.net/S/156001) |
| [マリーの架空世界](../data/songs/marry-no-kakuu-sekai.json) | [VocaDB](https://vocadb.net/S/25902) |
| [白雪～shirayuki～](../data/songs/snow-white.json) | [VocaDB](https://vocadb.net/S/11017) |
| [紅一葉](../data/songs/akahitoha.json) | [VocaDB](https://vocadb.net/S/8734) |
| [まにまに](../data/songs/manimani.json) | [VocaDB](https://vocadb.net/S/401491) |
| [沈みゆく哀](../data/songs/shizumi-yuku-ai.json) | [VocaDB](https://vocadb.net/S/57161) |
| [弱虫モンブラン](../data/songs/yowamushi-mont-blanc.json) | [VocaDB](https://vocadb.net/S/1268) |
| [罪の名前](../data/songs/tsumi-no-namae.json) | [VocaDB](https://vocadb.net/S/121112) |
| [D/N/A](../data/songs/d-n-a.json) | [VocaDB](https://vocadb.net/S/768497) |
| [君が生まれた日](../data/songs/kimi-ga-umareta-hi.json) | [VocaDB](https://vocadb.net/S/2291) |
| [Yellow](../data/songs/yellow.json) | [VocaDB](https://vocadb.net/S/2905) |
| [nuit](../data/songs/night.json) | [VocaDB](https://vocadb.net/S/173897) |
| [ほころび](../data/songs/hokorobi.json) | [VocaDB](https://vocadb.net/S/21614) |
| [glow](../data/songs/glow.json) | [VocaDB](https://vocadb.net/S/1797) |
| [歌に形はないけれど](../data/songs/uta-ni-katachi-wa-nai-keredo.json) | [VocaDB](https://vocadb.net/S/2322) |
| [ray](../data/songs/ray.json) | [VocaDB](https://vocadb.net/S/50721) |
| [ニア](../data/songs/near.json) | [VocaDB](https://vocadb.net/S/160448) |
| [ド屑](../data/songs/dokuzu.json) | [VocaDB](https://vocadb.net/S/389724) |
| [オノマトペメガネ](../data/songs/onomatopoeia-megane.json) | [VocaDB](https://vocadb.net/S/68478) |
| [死別](../data/songs/shibetsu.json) | [VocaDB](https://vocadb.net/S/606220) |
| [花めづる君](../data/songs/hanamezuru-kimi.json) | [VocaDB](https://vocadb.net/S/342023) |
| [39](../data/songs/vocadb-14480.json) | [VocaDB](https://vocadb.net/S/14480) |
| [愛されなくても君がいる](../data/songs/aisarenakute-mo-kimi-ga-iru.json) | [VocaDB](https://vocadb.net/S/284993) |
| [Blessing](../data/songs/blessing.json) | [VocaDB](https://vocadb.net/S/50703) |
| [空に免じて](../data/songs/sora-ni-menjite.json) | [VocaDB](https://vocadb.net/S/954657) |
| [アリスブルー](../data/songs/alice-blue.json) | [VocaDB](https://vocadb.net/S/330937) |
| [その一秒スローモーション](../data/songs/sono-ichibyou-slow-motion.json) | [VocaDB](https://vocadb.net/S/1329) |
| [群青讃歌](../data/songs/gunjou-sanka.json) | [VocaDB](https://vocadb.net/S/356981) |
| [ファシネイター](../data/songs/fascinator.json) | [VocaDB](https://vocadb.net/S/891732) |
| [いのちの歌](../data/songs/inochi-no-uta.json) | [VocaDB](https://vocadb.net/S/2947) |
| [ARiA](../data/songs/aria.json) | [VocaDB](https://vocadb.net/S/1723) |
| [僕のサイノウ](../data/songs/boku-no-sainou.json) | [VocaDB](https://vocadb.net/S/1503) |
| [カゲロウデイズ](../data/songs/kagerou-daze.json) | [VocaDB](https://vocadb.net/S/4979) |
| [Catch the Wave](../data/songs/catch-the-wave.json) | [VocaDB](https://vocadb.net/S/251481) |
| [電波中毒ガール](../data/songs/denpa-chuudoku-girl.json) | [VocaDB](https://vocadb.net/S/56582) |
| [アディショナルメモリー](../data/songs/additional-memory.json) | [VocaDB](https://vocadb.net/S/203445) |
| [ももいろの鍵](../data/songs/momoiro-no-kagi.json) | [VocaDB](https://vocadb.net/S/495666) |
| [ラストラス](../data/songs/lustrous.json) | [VocaDB](https://vocadb.net/S/789209) |
| [T氏の話を信じるな](../data/songs/t-shi-no-hanashi-o-shinjiru-na.json) | [VocaDB](https://vocadb.net/S/805591) |
| [キャットフード](../data/songs/cat-food.json) | [VocaDB](https://vocadb.net/S/1024) |
| [月光潤色ガール](../data/songs/gekkou-junshoku-girl.json) | [VocaDB](https://vocadb.net/S/75678) |
| [少女ケシゴム](../data/songs/shoujo-keshigomu.json) | [VocaDB](https://vocadb.net/S/45753) |
| [積み木の人形](../data/songs/tsumiki-no-ningyou.json) | [VocaDB](https://vocadb.net/S/1502) |
| [1/6 -out of the gravity-](../data/songs/1-6-out-of-the-gravity.json) | [VocaDB](https://vocadb.net/S/8246) |
| [夏に去りし君を想フ](../data/songs/natsu-ni-sarishi-kimi-o-omou.json) | [VocaDB](https://vocadb.net/S/1556) |
| [むかしむかしのきょうのぼく](../data/songs/mukashi-mukashi-no-kyou-no-boku.json) | [VocaDB](https://vocadb.net/S/1273) |
| [自傷無色](../data/songs/jishou-mushoku.json) | [VocaDB](https://vocadb.net/S/21604) |
| [千年の独奏歌](../data/songs/sennen-no-dokusouka.json) | [VocaDB](https://vocadb.net/S/3155) |
| [鎖の少女](../data/songs/kusari-no-shoujo.json) | [VocaDB](https://vocadb.net/S/2655) |
| [she](../data/songs/she.json) | [VocaDB](https://vocadb.net/S/286251) |
| [新人類](../data/songs/shinjinrui.json) | [VocaDB](https://vocadb.net/S/480295) |
| [ブレス・ユア・ブレス](../data/songs/bless-your-breath.json) | [VocaDB](https://vocadb.net/S/234901) |
| [サイハテ](../data/songs/saihate.json) | [VocaDB](https://vocadb.net/S/459) |
| [セカイ](../data/songs/sekai.json) | [VocaDB](https://vocadb.net/S/290231) |
| [東京レトロ](../data/songs/tokyo-retro.json) | [VocaDB](https://vocadb.net/S/31714) |
| [空奏列車](../data/songs/kuusou-ressha.json) | [VocaDB](https://vocadb.net/S/81431) |
| [SnowMix♪](../data/songs/snowmix.json) | [VocaDB](https://vocadb.net/S/460669) |
| [タイムマシン](../data/songs/time-machine.json) | [VocaDB](https://vocadb.net/S/1354) |
| [39みゅーじっく!](../data/songs/39-music.json) | [VocaDB](https://vocadb.net/S/127519) |
| [エンパープル](../data/songs/empurple.json) | [VocaDB](https://vocadb.net/S/642538) |
| [ハオ](../data/songs/hao.json) | [VocaDB](https://vocadb.net/S/640212) |
| [四角い地球を丸くする](../data/songs/shikakui-chikyuu-o-maruku-suru.json) | [VocaDB](https://vocadb.net/S/178433) |
| [勘違い性反希望症](../data/songs/kanchigai-seihan-kiboushou.json) | [VocaDB](https://vocadb.net/S/294038) |
| [Blue Star](../data/songs/blue-star.json) | [VocaDB](https://vocadb.net/S/105439) |
| [8.39](../data/songs/vocadb-252103.json) | [VocaDB](https://vocadb.net/S/252103) |
| [繰り返し一粒](../data/songs/kurikaeshi-hitotsubu.json) | [VocaDB](https://vocadb.net/S/8645) |
| [スターナイトスノウ](../data/songs/star-night-snow.json) | [VocaDB](https://vocadb.net/S/143132) |
| [失敗作少女](../data/songs/shippaisaku-shoujo.json) | [VocaDB](https://vocadb.net/S/79675) |
| [モア！ジャンプ！モア！](../data/songs/more-jump-more.json) | [VocaDB](https://vocadb.net/S/517576) |
| [桜ノ雨](../data/songs/sakura-no-ame.json) | [VocaDB](https://vocadb.net/S/8741) |
| [Starduster](../data/songs/starduster.json) | [VocaDB](https://vocadb.net/S/2913) |
| [猛独が襲う](../data/songs/moudoku-ga-osou.json) | [VocaDB](https://vocadb.net/S/159274) |
| [こちら、幸福安心委員会です。](../data/songs/kochira-koufuku-anshin-iinkai-desu.json) | [VocaDB](https://vocadb.net/S/13260) |
| [幸せになれる隠しコマンドがあるらしい](../data/songs/shiawase-ni-nareru-kakushi-command-ga-arurashii.json) | [VocaDB](https://vocadb.net/S/24239) |
| [恋の恋による恋のための恋](../data/songs/koi-no-koi-ni-yoru-koi-no-tame-no-koi.json) | [VocaDB](https://vocadb.net/S/244291) |
| [ゼロトーキング](../data/songs/zero-talking.json) | [VocaDB](https://vocadb.net/S/540081) |
| [好き！雪！本気マジック](../data/songs/suki-yuki-maji-magic.json) | [VocaDB](https://vocadb.net/S/47354) |
| [Gimme×Gimme](../data/songs/gimmegimme.json) | [VocaDB](https://vocadb.net/S/246033) |
| [嗚咽](../data/songs/oetsu.json) | [VocaDB](https://vocadb.net/S/42902) |
| [文学者の恋文](../data/songs/bungakusha-no-koibumi.json) | [VocaDB](https://vocadb.net/S/59447) |
| [虹色蝶々](../data/songs/nijiiro-chouchou.json) | [VocaDB](https://vocadb.net/S/11018) |
| [僕が夢を捨てて大人になるまで](../data/songs/boku-ga-yume-o-sutete-otona-ni-naru-made.json) | [VocaDB](https://vocadb.net/S/207476) |
| [Iなんです](../data/songs/i-nan-desu.json) | [VocaDB](https://vocadb.net/S/455434) |
| [心予報](../data/songs/kokoro-yohou.json) | [VocaDB](https://vocadb.net/S/384155) |
| [マインドブランド](../data/songs/mind-brand.json) | [VocaDB](https://vocadb.net/S/89474) |
| [ブループラネット](../data/songs/blue-planet.json) | [VocaDB](https://vocadb.net/S/525396) |
| [夜に駆ける](../data/songs/yoru-ni-kakeru.json) | [VocaDB](https://vocadb.net/S/262741) |
| [おじゃま虫](../data/songs/ojamamushi.json) | [VocaDB](https://vocadb.net/S/48030) |
| [おじゃま虫Ⅱ](../data/songs/ojamamushi-ii.json) | [VocaDB](https://vocadb.net/S/340768) |
| [針鼠](../data/songs/harinezumi.json) | [VocaDB](https://vocadb.net/S/131093) |
| [ラストスコア](../data/songs/last-score.json) | [VocaDB](https://vocadb.net/S/350191) |
| [しかばねの踊り](../data/songs/shikabane-no-odori.json) | [VocaDB](https://vocadb.net/S/36002) |
| [転生林檎](../data/songs/tensei-ringo.json) | [VocaDB](https://vocadb.net/S/411304) |
| [Hand in Hand](../data/songs/hand-in-hand.json) | [VocaDB](https://vocadb.net/S/89726) |
| [DECORATOR](../data/songs/decorator.json) | [VocaDB](https://vocadb.net/S/45245) |
| [夕日坂](../data/songs/yuuhizaka.json) | [VocaDB](https://vocadb.net/S/7714) |
| [Alice in 冷凍庫](../data/songs/alice-in-reitouko.json) | [VocaDB](https://vocadb.net/S/114987) |
| [White Landscape](../data/songs/white-landscape.json) | [VocaDB](https://vocadb.net/S/146572) |
| [アウターサイエンス](../data/songs/outer-science.json) | [VocaDB](https://vocadb.net/S/28646) |
| [八十八鍵の宇宙](../data/songs/hachi-juu-hachi-ken-no-uchuu.json) | [VocaDB](https://vocadb.net/S/146574) |
| [心象蜃気楼](../data/songs/shinshou-shinkirou.json) | [VocaDB](https://vocadb.net/S/137377) |
| [酔いどれ知らず](../data/songs/yoidore-shirazu.json) | [VocaDB](https://vocadb.net/S/404609) |
| [おどりゃんせ](../data/songs/odoryanse.json) | [VocaDB](https://vocadb.net/S/138174) |
| [サイエンス](../data/songs/science.json) | [VocaDB](https://vocadb.net/S/713636) |
| [明正ロマン](../data/songs/meishou-romance.json) | [VocaDB](https://vocadb.net/S/28602) |
| [おべか](../data/songs/obeka.json) | [VocaDB](https://vocadb.net/S/662691) |
| [㋰責任集合体](../data/songs/musekinin-shuugoutai.json) | [VocaDB](https://vocadb.net/S/626191) |
| [ライアーダンサー](../data/songs/liar-dancer.json) | [VocaDB](https://vocadb.net/S/506793) |
| [ウルトラトレーラー](../data/songs/ultra-trailer.json) | [VocaDB](https://vocadb.net/S/552563) |
| [ちっちゃな私](../data/songs/chiccha-na-watashi.json) | [VocaDB](https://vocadb.net/S/520602) |
| [いいねってYEAH!](../data/songs/ii-ne-tte-yeah.json) | [VocaDB](https://vocadb.net/S/415813) |
| [少女人形の見た夢](../data/songs/shoujo-ningyou-no-mita-yume.json) | [VocaDB](https://vocadb.net/S/97903) |
| [ニヒルと水没都市](../data/songs/nihil-to-suibotsu-toshi.json) | [VocaDB](https://vocadb.net/S/102209) |
| [えれくとりっく・えんじぇぅ](../data/songs/electric-angel.json) | [VocaDB](https://vocadb.net/S/2915) |
| [表裏一体](../data/songs/hyouri-ittai.json) | [VocaDB](https://vocadb.net/S/192629) |
| [病名は愛だった](../data/songs/byoumei-wa-ai-datta.json) | [VocaDB](https://vocadb.net/S/164262) |
| [アマツキツネ](../data/songs/amatsu-kitsune.json) | [VocaDB](https://vocadb.net/S/15691) |
| [怪盗・窪園チヨコは絶対ミスらない](../data/songs/kaitou-kubozono-chiyoko-wa-zettai-misuranai.json) | [VocaDB](https://vocadb.net/S/1825) |
| [少女A](../data/songs/shoujo-a.json) | [VocaDB](https://vocadb.net/S/42111) |
| [モザイクロール](../data/songs/mozaik-role.json) | [VocaDB](https://vocadb.net/S/1381) |
| [アイラ](../data/songs/aira.json) | [VocaDB](https://vocadb.net/S/89641) |
| [マネマネサイコトロピック](../data/songs/mane-mane-psychotropic.json) | [VocaDB](https://vocadb.net/S/37948) |
| [スーサイドパレヱド](../data/songs/suicide-parade.json) | [VocaDB](https://vocadb.net/S/161926) |
| [あしゅらしゅら](../data/songs/ashura-shura.json) | [VocaDB](https://vocadb.net/S/286030) |
| [強風オールバック](../data/songs/kyoufuu-all-back.json) | [VocaDB](https://vocadb.net/S/482572) |
| [熱異常](../data/songs/netsu-ijou.json) | [VocaDB](https://vocadb.net/S/443534) |
| [シェーマ](../data/songs/shamer.json) | [VocaDB](https://vocadb.net/S/295177) |
