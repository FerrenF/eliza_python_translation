CACM_1966_01_DOCTOR_script = ";\n" \
                             "; Joseph Weizenbaum's DOCTOR script for ELIZA\n" \
                             ";\n" \
                             "; This is a verbatim transcription of the script on page 44 of the\n" \
                             "; January 1966 edition of Communications of the ACM, with the following\n" \
                             "; caveats:\n" \
                             ";\n" \
                             "; a) Whitespace has been added to help reveal the structure of the script.\n" \
                             "; b) In the CACM paper six lines were printed twice adjacent to each\n" \
                             ";    other (with exactly 34 lines between each duplicate), making the\n" \
                             ";    structure nonsensical. These duplicates have been commented out of\n" \
                             ";    this transcription.\n" \
                             "; c) There were no comments in the script in the CACM paper.\n" \
                             ";\n" \
                             "\n" \
                             "\n" \
                             "(HOW DO YOU DO.  PLEASE TELL ME YOUR PROBLEM)\n" \
                             "\n" \
                             "START\n" \
                             "\n" \
                             "(SORRY\n" \
                             "    ((0)\n" \
                             "        (PLEASE DON'T APOLIGIZE)\n" \
                             "        (APOLOGIES ARE NOT NECESSARY)\n" \
                             "        (WHAT FEELINGS DO YOU HAVE WHEN YOU APOLOGIZE)\n" \
                             "        (I'VE TOLD YOU THAT APOLOGIES ARE NOT REQUIRED)))\n" \
                             "\n" \
                             "(DONT = DON'T)\n" \
                             "(CANT = CAN'T)\n" \
                             "(WONT = WON'T)\n" \
                             "\n" \
                             "(REMEMBER 5\n" \
                             "    ((0 YOU REMEMBER 0)\n" \
                             "         (DO YOU OFTEN THINK OF 4)\n" \
                             "         (DOES THINKING OF 4 BRING ANYTHING ELSE TO MIND)\n" \
                             "         (WHAT ELSE DO YOU REMEMBER)\n" \
                             "         (WHY DO YOU REMEMBER 4 JUST NOW)\n" \
                             "         (WHAT IN THE PRESENT SITUATION REMINDS YOU OF 4)\n" \
                             "         (WHAT IS THE CONNECTION BETWEEN ME AND 4))\n" \
                             "    ((0 DO I REMEMBER 0)\n" \
                             "         (DID YOU THINK I WOULD FORGET 5)\n" \
                             "         (WHY DO YOU THINK I SHOULD RECALL 5 NOW)\n" \
                             "         (WHAT ABOUT 5)\n" \
                             "         (=WHAT)\n" \
                             "         (YOU MENTIONED 5))\n" \
                             "    ((0)\n" \
                             "         (NEWKEY)))\n" \
                             "\n" \
                             "(IF 3\n" \
                             "    ((0 IF 0)\n" \
                             "        (DO YOU THINK ITS LIKELY THAT 3)\n" \
                             "        (DO YOU WISH THAT 3)\n" \
                             "        (WHAT DO YOU THINK ABOUT 3)\n" \
                             "        (REALLY, 2 3)))\n" \
                             "; duplicate line removed: (WHAT DO YOU THINK ABOUT 3) (REALLY, 2 3)))\n" \
                             "\n" \
                             "(DREAMT 4\n" \
                             "    ((0 YOU DREAMT 0)\n" \
                             "        (REALLY, 4)\n" \
                             "        (HAVE YOU EVER FANTASIED 4 WHILE YOU WERE AWAKE)\n" \
                             "        (HAVE YOU DREAMT 4 BEFORE)\n" \
                             "        (=DREAM)\n" \
                             "        (NEWKEY)))\n" \
                             "\n" \
                             "(DREAMED = DREAMT 4\n" \
                             "    (=DREAMT))\n" \
                             "\n" \
                             "(DREAM 3\n" \
                             "    ((0)\n" \
                             "        (WHAT DOES THAT DREAM SUGGEST TO YOU)\n" \
                             "        (DO YOU DREAM OFTEN)\n" \
                             "        (WHAT PERSONS APPEAR IN YOUR DREAMS)\n" \
                             "        (DON'T YOU BELIEVE THAT DREAM HAS SOMETHING TO DO WITH YOUR PROBLEM)\n" \
                             "        (NEWKEY)))\n" \
                             "\n" \
                             "(DREAMS = DREAM 3\n" \
                             "    (=DREAM))\n" \
                             "\n" \
                             "(HOW\n" \
                             "    (=WHAT))\n" \
                             "(WHEN\n" \
                             "    (=WHAT))\n" \
                             "(ALIKE 10\n" \
                             "    (=DIT))\n" \
                             "(SAME 10\n" \
                             "    (=DIT))\n" \
                             "(CERTAINLY\n" \
                             "    (=YES))\n" \
                             "\n" \
                             "(FEEL DLIST(/BELIEF))\n" \
                             "(THINK DLIST(/BELIEF))\n" \
                             "(BELIEVE DLIST(/BELIEF))\n" \
                             "(WISH DLIST(/BELIEF))\n" \
                             "\n" \
                             "(MEMORY MY\n" \
                             "    (0 YOUR 0 = LETS DISCUSS FURTHER WHY YOUR 3)\n" \
                             "    (0 YOUR 0 = EARLIER YOU SAID YOUR 3)\n" \
                             "    (0 YOUR 0 = BUT YOUR 3)\n" \
                             "    (0 YOUR 0 = DOES THAT HAVE ANYTHING TO DO WITH THE FACT THAT YOUR 3))\n" \
                             "\n" \
                             "(NONE\n" \
                             "    ((0)\n" \
                             "        (I AM NOT SURE I UNDERSTAND YOU FULLY)\n" \
                             "        (PLEASE GO ON)\n" \
                             "        (WHAT DOES THAT SUGGEST TO YOU)\n" \
                             "        (DO YOU FEEL STRONGLY ABOUT DISCUSSING SUCH THINGS)))\n" \
                             "\n" \
                             "(PERHAPS\n" \
                             "    ((0)\n" \
                             "        (YOU DON'T SEEM QUITE CERTAIN)\n" \
                             "        (WHY THE UNCERTAIN TONE)\n" \
                             "        (CAN'T YOU BE MORE POSITIVE)\n" \
                             "        (YOU AREN'T SURE)\n" \
                             "        (DON'T YOU KNOW)))\n" \
                             "\n" \
                             "(MAYBE\n" \
                             "    (=PERHAPS))\n" \
                             "\n" \
                             "(NAME 15\n" \
                             "    ((0)\n" \
                             "        (I AM NOT INTERESTED IN NAMES)\n" \
                             "        (I'VE TOLD YOU BEFORE, I DON'T CARE ABOUT NAMES - PLEASE CONTINUE)))\n" \
                             "; duplicate line removed: PLEASE CONTINUE)) )\n" \
                             "\n" \
                             "(DEUTSCH\n" \
                             "    (=XFREMD))\n" \
                             "(FRANCAIS\n" \
                             "    (=XFREMD))\n" \
                             "(ITALIANO\n" \
                             "    (=XFREMD))\n" \
                             "(ESPANOL\n" \
                             "    (=XFREMD))\n" \
                             "\n" \
                             "(XFREMD\n" \
                             "    ((0)\n" \
                             "        (I AM SORRY, I SPEAK ONLY ENGLISH)))\n" \
                             "\n" \
                             "(HELLO\n" \
                             "    ((0)\n" \
                             "        (HOW DO YOU DO.  PLEASE STATE YOUR PROBLEM)))\n" \
                             "\n" \
                             "(COMPUTER 50\n" \
                             "    ((0)\n" \
                             "        (DO COMPUTERS WORRY YOU)\n" \
                             "        (WHY DO YOU MENTION COMPUTERS)\n" \
                             "        (WHAT DO YOU THINK MACHINES HAVE TO DO WITH YOUR PROBLEM)\n" \
                             "        (DON'T YOU THINK COMPUTERS CAN HELP PEOPLE)\n" \
                             "        (WHAT ABOUT MACHINES WORRIES YOU)\n" \
                             "        (WHAT DO YOU THINK ABOUT MACHINES)))\n" \
                             "\n" \
                             "(MACHINE 50\n" \
                             "    (=COMPUTER))\n" \
                             "(MACHINES 50\n" \
                             "    (=COMPUTER))\n" \
                             "(COMPUTERS 50\n" \
                             "    (=COMPUTER))\n" \
                             "\n" \
                             "(AM = ARE\n" \
                             "    ((0 ARE YOU 0)\n" \
                             "        (DO YOU BELIEVE YOU ARE 4)\n" \
                             "        (WOULD YOU WANT TO BE 4)\n" \
                             "        (YOU WISH I WOULD TELL YOU YOU ARE 4)\n" \
                             "        (WHAT WOULD IT MEAN IF YOU WERE 4)\n" \
                             "        (=WHAT))\n" \
                             "    ((0)\n" \
                             "        (WHY DO YOU SAY 'AM')\n" \
                             "        (I DON'T UNDERSTAND THAT)))\n" \
                             "\n" \
                             "(ARE\n" \
                             "    ((0 ARE I 0)\n" \
                             "        (WHY ARE YOU INTERESTED IN WHETHER I AM 4 OR NOT)\n" \
                             "        (WOULD YOU PREFER IF I WEREN'T 4)\n" \
                             "        (PERHAPS I AM 4 IN YOUR FANTASIES)\n" \
                             "        (DO YOU SOMETIMES THINK I AM 4)\n" \
                             "        (=WHAT))\n" \
                             "    ((0 ARE 0)\n" \
                             "        (DID YOU THINK THEY MIGHT NOT BE 3)\n" \
                             "        (WOULD YOU LIKE IT IF THEY WERE NOT 3)\n" \
                             "        (WHAT IF THEY WERE NOT 3)\n" \
                             "        (POSSIBLY THEY ARE 3)))\n" \
                             "\n" \
                             "(YOUR = MY\n" \
                             "    ((0 MY 0)\n" \
                             "        (WHY ARE YOU CONCERNED OVER MY 3)\n" \
                             "        (WHAT ABOUT YOUR OWN 3)\n" \
                             "        (ARE YOU WORRIED ABOUT SOMEONE ELSES 3)\n" \
                             "        (REALLY, MY 3)))\n" \
                             "\n" \
                             "(WAS 2\n" \
                             "    ((0 WAS YOU 0)\n" \
                             "        (WHAT IF YOU WERE 4)\n" \
                             "        (DO YOU THINK YOU WERE 4)\n" \
                             "        (WERE YOU 4)\n" \
                             "        (WHAT WOULD IT MEAN IF YOU WERE 4)\n" \
                             "        (WHAT DOES ' 4 ' SUGGEST TO YOU)\n" \
                             "        (=WHAT))\n" \
                             "    ((0 YOU WAS 0)\n" \
                             "        (WERE YOU REALLY)\n" \
                             "        (WHY DO YOU TELL ME YOU WERE 4 NOW)\n" \
                             "; duplicate line removed: (WERE YOU REALLY) (WHY DO YOU TELL ME YOU WERE 4 NOW)\n" \
                             "        (PERHAPS I ALREADY KNEW YOU WERE 4))\n" \
                             "    ((0 WAS I 0)\n" \
                             "        (WOULD YOU LIKE TO BELIEVE I WAS 4)\n" \
                             "        (WHAT SUGGESTS THAT I WAS 4)\n" \
                             "        (WHAT DO YOU THINK)\n" \
                             "        (PERHAPS I WAS 4)\n" \
                             "        (WHAT IF I HAD BEEN 4))\n" \
                             "    ((0)\n" \
                             "        (NEWKEY)))\n" \
                             "\n" \
                             "(WERE = WAS\n" \
                             "    (=WAS))\n" \
                             "(ME = YOU)\n" \
                             "\n" \
                             "(YOU'RE = I'M\n" \
                             "    ((0 I'M 0)\n" \
                             "        (PRE (I ARE 3) (=YOU))))\n" \
                             "\n" \
                             "(I'M = YOU'RE\n" \
                             "    ((0 YOU'RE 0)\n" \
                             "        (PRE (YOU ARE 3) (=I))))\n" \
                             "\n" \
                             "(MYSELF = YOURSELF)\n" \
                             "(YOURSELF = MYSELF)\n" \
                             "\n" \
                             "(MOTHER DLIST(/NOUN FAMILY))\n" \
                             "(MOM = MOTHER DLIST(/ FAMILY))\n" \
                             "(DAD = FATHER DLIST(/ FAMILY))\n" \
                             "(FATHER DLIST(/NOUN FAMILY))\n" \
                             "(SISTER DLIST(/FAMILY))\n" \
                             "(BROTHER DLIST(/FAMILY))\n" \
                             "(WIFE DLIST(/FAMILY))\n" \
                             "(CHILDREN DLIST(/FAMILY))\n" \
                             "\n" \
                             "(I = YOU\n" \
                             "    ((0 YOU (* WANT NEED) 0)\n" \
                             "        (WHAT WOULD IT MEAN TO YOU IF YOU GOT 4)\n" \
                             "        (WHY DO YOU WANT 4)\n" \
                             "        (SUPPOSE YOU GOT 4 SOON)\n" \
                             "        (WHAT IF YOU NEVER GOT 4)\n" \
                             "        (WHAT WOULD GETTING 4 MEAN TO YOU)\n" \
                             "        (WHAT DOES WANTING 4 HAVE TO DO WITH THIS DISCUSSION))\n" \
                             "    ((0 YOU ARE 0 (*SAD UNHAPPY DEPRESSED SICK ) 0)\n" \
                             "        (I AM SORRY TO HEAR YOU ARE 5)\n" \
                             "        (DO YOU THINK COMING HERE WILL HELP YOU NOT TO BE 5)\n" \
                             "        (I'M SURE ITS NOT PLEASANT TO BE 5)\n" \
                             "        (CAN YOU EXPLAIN WHAT MADE YOU 5))\n" \
                             "    ((0 YOU ARE 0 (*HAPPY ELATED GLAD BETTER) 0)\n" \
                             "        (HOW HAVE I HELPED YOU TO BE 5)\n" \
                             "        (HAS YOUR TREATMENT MADE YOU 5)\n" \
                             "        (WHAT MAKES YOU 5 JUST NOW)\n" \
                             "        (CAN YOU EXPLAIN WHY YOU ARE SUDDENLY 5))\n" \
                             "    ((0 YOU WAS 0)\n" \
                             "        (=WAS))\n" \
                             "; duplicate line removed: ((0 YOU WAS 0) (=WAS))\n" \
                             "    ((0 YOU (/BELIEF) YOU 0)\n" \
                             "        (DO YOU REALLY THINK SO)\n" \
                             "        (BUT YOU ARE NOT SURE YOU 5)\n" \
                             "        (DO YOU REALLY DOUBT YOU 5))\n" \
                             "    ((0 YOU 0 (/BELIEF) 0 I 0)\n" \
                             "        (=YOU))\n" \
                             "    ((0 YOU ARE 0)\n" \
                             "        (IS IT BECAUSE YOU ARE 4 THAT YOU CAME TO ME)\n" \
                             "        (HOW LONG HAVE YOU BEEN 4)\n" \
                             "        (DO YOU BELIEVE IT NORMAL TO BE 4)\n" \
                             "        (DO YOU ENJOY BEING 4))\n" \
                             "    ((0 YOU (* CAN'T CANNOT) 0)\n" \
                             "        (HOW DO YOU KNOW YOU CAN'T 4)\n" \
                             "        (HAVE YOU TRIED)\n" \
                             "        (PERHAPS YOU COULD 4 NOW)\n" \
                             "        (DO YOU REALLY WANT TO BE ABLE TO 4))\n" \
                             "    ((0 YOU DON'T 0)\n" \
                             "        (DON'T YOU REALLY 4)\n" \
                             "        (WHY DON'T YOU 4)\n" \
                             "        (DO YOU WISH TO BE ABLE TO 4)\n" \
                             "        (DOES THAT TROUBLE YOU))\n" \
                             "    ((0 YOU FEEL 0)\n" \
                             "        (TELL ME MORE ABOUT SUCH FEELINGS)\n" \
                             "        (DO YOU OFTEN FEEL 4)\n" \
                             "        (DO YOU ENJOY FEELING 4)\n" \
                             "        (OF WHAT DOES FEELING 4 REMIND YOU))\n" \
                             "    ((0 YOU 0 I 0)\n" \
                             "        (PERHAPS IN YOUR FANTASY WE 3 EACH OTHER)\n" \
                             "        (DO YOU WISH TO 3 ME)\n" \
                             "        (YOU SEEM TO NEED TO 3 ME)\n" \
                             "        (DO YOU 3 ANYONE ELSE))\n" \
                             "    ((0)\n" \
                             "        (YOU SAY 1)\n" \
                             "        (CAN YOU ELABORATE ON THAT)\n" \
                             "        (DO YOU SAY 1 FOR SOME SPECIAL REASON)\n" \
                             "        (THAT'S QUITE INTERESTING)))\n" \
                             "\n" \
                             "(YOU = I\n" \
                             "    ((0 I REMIND YOU OF 0)\n" \
                             "        (=DIT))\n" \
                             "    ((0 I ARE 0)\n" \
                             "        (WHAT MAKES YOU THINK I AM 4)\n" \
                             "        (DOES IT PLEASE YOU TO BELIEVE I AM 4)\n" \
                             "        (DO YOU SOMETIMES WISH YOU WERE 4)\n" \
                             "        (PERHAPS YOU WOULD LIKE TO BE 4))\n" \
                             "    ((0 I 0 YOU)\n" \
                             "        (WHY DO YOU THINK I 3 YOU)\n" \
                             "        (YOU LIKE TO THINK I 3 YOU - DON'T YOU)\n" \
                             "        (WHAT MAKES YOU THINK I 3 YOU)\n" \
                             "        (REALLY, I 3 YOU)\n" \
                             "        (DO YOU WISH TO BELIEVE I 3 YOU)\n" \
                             "; duplicate line removed: (REALLY, I 3 YOU) (DO YOU WISH TO BELIEVE I 3 YOU)\n" \
                             "        (SUPPOSE I DID 3 YOU - WHAT WOULD THAT MEAN)\n" \
                             "        (DOES SOMEONE ELSE BELIEVE I 3 YOU))\n" \
                             "    ((0 I 0)\n" \
                             "        (WE WERE DISCUSSING YOU - NOT ME)\n" \
                             "        (OH, I 3)\n" \
                             "        (YOU'RE NOT REALLY TALKING ABOUT ME - ARE YOU)\n" \
                             "        (WHAT ARE YOUR FEELINGS NOW)))\n" \
                             "\n" \
                             "(YES\n" \
                             "    ((0)\n" \
                             "        (YOU SEEM QUITE POSITIVE)\n" \
                             "        (YOU ARE SURE)\n" \
                             "        (I SEE)\n" \
                             "        (I UNDERSTAND)))\n" \
                             "\n" \
                             "(NO\n" \
                             "    ((0)\n" \
                             "        (ARE YOU SAYING 'NO' JUST TO BE NEGATIVE)\n" \
                             "        (YOU ARE BEING A BIT NEGATIVE)\n" \
                             "        (WHY NOT)\n" \
                             "        (WHY 'NO')))\n" \
                             "\n" \
                             "(MY = YOUR 2\n" \
                             "    ((0 YOUR 0 (/FAMILY) 0)\n" \
                             "        (TELL ME MORE ABOUT YOUR FAMILY)\n" \
                             "        (WHO ELSE IN YOUR FAMILY 5)\n" \
                             "        (YOUR 4)\n" \
                             "        (WHAT ELSE COMES TO MIND WHEN YOU THINK OF YOUR 4))\n" \
                             "    ((0 YOUR 0)\n" \
                             "        (YOUR 3)\n" \
                             "        (WHY DO YOU SAY YOUR 3)\n" \
                             "        (DOES THAT SUGGEST ANYTHING ELSE WHICH BELONGS TO YOU)\n" \
                             "        (IS IT IMPORTANT TO YOU THAT 2 3)))\n" \
                             "\n" \
                             "(CAN\n" \
                             "    ((0 CAN I 0)\n" \
                             "        (YOU BELIEVE I CAN 4 DON'T YOU)\n" \
                             "        (=WHAT)\n" \
                             "        (YOU WANT ME TO BE ABLE TO 4)\n" \
                             "        (PERHAPS YOU WOULD LIKE TO BE ABLE TO 4 YOURSELF))\n" \
                             "    ((0 CAN YOU 0)\n" \
                             "        (WHETHER OR NOT YOU CAN 4 DEPENDS ON YOU MORE THAN ON ME)\n" \
                             "        (DO YOU WANT TO BE ABLE TO 4)\n" \
                             "        (PERHAPS YOU DON'T WANT TO 4)\n" \
                             "        (=WHAT)))\n" \
                             "\n" \
                             "(WHAT\n" \
                             "    ((0)\n" \
                             "        (WHY DO YOU ASK)\n" \
                             "        (DOES THAT QUESTION INTEREST YOU)\n" \
                             "        (WHAT IS IT YOU REALLY WANT TO KNOW)\n" \
                             "        (ARE SUCH QUESTIONS MUCH ON YOUR MIND)\n" \
                             "        (WHAT ANSWER WOULD PLEASE YOU MOST)\n" \
                             "        (WHAT DO YOU THINK)\n" \
                             "        (WHAT COMES TO YOUR MIND WHEN YOU ASK THAT)\n" \
                             "        (HAVE YOU ASKED SUCH QUESTIONS BEFORE)\n" \
                             "        (HAVE YOU ASKED ANYONE ELSE)))\n" \
                             "\n" \
                             "(BECAUSE\n" \
                             "    ((0)\n" \
                             "        (IS THAT THE REAL REASON)\n" \
                             "        (DON'T ANY OTHER REASONS COME TO MIND)\n" \
                             "        (DOES THAT REASON SEEM TO EXPLAIN ANYTHING ELSE)\n" \
                             "        (WHAT OTHER REASONS MIGHT THERE BE)))\n" \
                             "\n" \
                             "(WHY\n" \
                             "    ((0 WHY DON'T I 0)\n" \
                             "        (DO YOU BELIEVE I DON'T 5)\n" \
                             "        (PERHAPS I WILL 5 IN GOOD TIME)\n" \
                             "        (SHOULD YOU 5 YOURSELF)\n" \
                             "        (YOU WANT ME TO 5)\n" \
                             "        (=WHAT))\n" \
                             "; duplicate line removed: (=WHAT))\n" \
                             "    ((0 WHY CAN'T YOU 0)\n" \
                             "        (DO YOU THINK YOU SHOULD BE ABLE TO 5)\n" \
                             "        (DO YOU WANT TO BE ABLE TO 5)\n" \
                             "        (DO YOU BELIEVE THIS WILL HELP YOU TO 5)\n" \
                             "        (HAVE YOU ANY IDEA WHY YOU CAN'T 5)\n" \
                             "        (=WHAT))\n" \
                             "    (=WHAT))\n" \
                             "\n" \
                             "(EVERYONE 2\n" \
                             "    ((0 (* EVERYONE EVERYBODY NOBODY NOONE) 0)\n" \
                             "        (REALLY, 2)\n" \
                             "        (SURELY NOT 2)\n" \
                             "        (CAN YOU THINK OF ANYONE IN PARTICULAR)\n" \
                             "        (WHO, FOR EXAMPLE)\n" \
                             "        (YOU ARE THINKING OF A VERY SPECIAL PERSON)\n" \
                             "        (WHO, MAY I ASK)\n" \
                             "        (SOMEONE SPECIAL PERHAPS)\n" \
                             "        (YOU HAVE A PARTICULAR PERSON IN MIND, DON'T YOU)\n" \
                             "        (WHO DO YOU THINK YOU'RE TALKING ABOUT)))\n" \
                             "\n" \
                             "(EVERYBODY 2\n" \
                             "    (= EVERYONE))\n" \
                             "(NOBODY 2\n" \
                             "    (= EVERYONE))\n" \
                             "(NOONE 2\n" \
                             "    (= EVERYONE))\n" \
                             "\n" \
                             "(ALWAYS 1\n" \
                             "    ((0)\n" \
                             "        (CAN YOU THINK OF A SPECIFIC EXAMPLE)\n" \
                             "        (WHEN)\n" \
                             "        (WHAT INCIDENT ARE YOU THINKING OF)\n" \
                             "        (REALLY, ALWAYS)))\n" \
                             "\n" \
                             "(LIKE 10\n" \
                             "    ((0 (*AM IS ARE WAS) 0 LIKE 0)\n" \
                             "        (=DIT))\n" \
                             "    ((0)\n" \
                             "        (NEWKEY)))\n" \
                             "\n" \
                             "(DIT\n" \
                             "    ((0)\n" \
                             "        (IN WHAT WAY)\n" \
                             "        (WHAT RESEMBLANCE DO YOU SEE)\n" \
                             "        (WHAT DOES THAT SIMILARITY SUGGEST TO YOU)\n" \
                             "        (WHAT OTHER CONNECTIONS DO YOU SEE)\n" \
                             "        (WHAT DO YOU SUPPOSE THAT RESEMBLANCE MEANS)\n" \
                             "        (WHAT IS THE CONNECTION, DO YOU SUPPOSE)\n" \
                             "        (COULD THERE REALLY BE SOME CONNECTION)\n" \
                             "        (HOW)))\n" \
                             "\n" \
                             "()\n" \
                             "\n" \
                             "; --- End of ELIZA script ---\n"