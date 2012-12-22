movie 'C:\projects\Ra3\PRODUC~1\Data\APTBUI~1\034A3~1.0-D\pc\Output\TACTIC~4\\TACTIC~1.eaf' &compressed // flash 7, total frames: 1, frame rate: 30 fps, 1024x768 px

  &defineButton 2
  
    &on     &overUpToOverDown
      &constants 'client', 'selectedTabButton', 'this', 'OnPressed'  
      &pushsdbgv 0							//'client'
      &pushsdbgm 1							//'selectedTabButton'
      &pushthisgv
      &equals
      &not
      &not
      &jnz label1      
      &gotoLabel '_down'
      &play
     label1:
      &pushthisgv
      &pushone
      &pushsdbgv 0							//'client'
      &dcallmp 3							// OnPressed()
    &end
  
    &on     &overDownToOverUp
      &constants 'client', 'selectedTabButton', 'this', 'OnClicked'  
      &pushsdbgv 0							//'client'
      &pushsdbgm 1							//'selectedTabButton'
      &pushthisgv
      &equals
      &not
      &not
      &jnz label1      
      &gotoLabel '_over'
      &play
      &pushthisgv
      &pushone
      &pushsdbgv 0							//'client'
      &dcallmp 3							// OnClicked()
     label1:
    &end
  
    &on     &idleToOverUp    ,&outDownToOverDown    ,&idleToOverDown
      &constants 'client', 'selectedTabButton', 'this', 'OnRollOver'  
      &pushsdbgv 0							//'client'
      &pushsdbgm 1							//'selectedTabButton'
      &pushthisgv
      &equals
      &not
      &not
      &jnz label1      
      &gotoLabel '_over'
      &play
     label1:
      &pushthisgv
      &pushone
      &pushsdbgv 0							//'client'
      &dcallmp 3							// OnRollOver()
    &end
  
    &on     &overUpToIdle    ,&overDownToOutDown    ,&overDownToIdle
      &constants 'client', 'selectedTabButton', 'this', 'OnRollOut'  
      &pushsdbgv 0							//'client'
      &pushsdbgm 1							//'selectedTabButton'
      &pushthisgv
      &equals
      &not
      &not
      &jnz label1      
      &gotoLabel '_up'
      &play
     label1:
      &pushthisgv
      &pushone
      &pushsdbgv 0							//'client'
      &dcallmp 3							// OnRollOut()
    &end
  &end // of defineButton 2

  &defineMovieClip 9 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 9

  &defineMovieClip 11 // total frames: 1
  &end // of defineMovieClip 11

  &defineMovieClip 12 // total frames: 35

    &frame 4
      &stop
    &end // of frame 4

    &frame 34
      &gotoLabel '_on'
      &play
    &end // of frame 34
  &end // of defineMovieClip 12

  &defineMovieClip 15 // total frames: 1
  &end // of defineMovieClip 15

  &defineMovieClip 20 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 20

  &defineMovieClip 25 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 25

  &defineMovieClip 30 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 30

  &defineMovieClip 35 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 35

  &defineMovieClip 40 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 40

  &defineMovieClip 45 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 45

  &defineMovieClip 46 // total frames: 30

    &frame 0
      &pushs '_'
      &pushsgv '_parent'
      &pushsgm 'iconLabel'
      &add
      &gotoAndStop    &end // of frame 0
  &end // of defineMovieClip 46

  &defineMovieClip 53 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 53

  &defineMovieClip 56 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 56

  &defineMovieClip 59 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 59

  &defineMovieClip 62 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 62

  &defineMovieClip 65 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 65

  &defineMovieClip 68 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 68

  &defineMovieClip 71 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 71

  &defineMovieClip 72 // total frames: 30

    &frame 0
      &pushs '_'
      &pushsgv '_parent'
      &pushsgm 'iconLabel'
      &add
      &gotoAndStop    &end // of frame 0
  &end // of defineMovieClip 72

  &defineMovieClip 73 // total frames: 40

    &frame 0
      &constants 'client', '_parent'  
      &pushsdbgv 0							//'client'
      &pushundef
      &equals
      &not
      &jnz label1      
      &pushsdb 0							//'client'
      &pushsdbgv 1							//'_parent'
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 73
  
  &exportAssets
    73 &as 'TabButton'
  &end // of exportAssets

  &defineMovieClip 74 // total frames: 1
  &end // of defineMovieClip 74

  &defineMovieClip 75 // total frames: 1

    &frame 0
      &constants 'commandList', 'Pointer', 'encode', 'tabHelpSite', 'FSCommand:', 'OnTabPressed', 'qualifyName', '', 'OnTabRollOver', 'OnTabRollOut', 'GetCommandList', 'GetTabHelpSite', 'onUnload', 'initialized', 'disableCommandButtonLoadAnim', 'TacticalHUDCommandListBox.swf', 'loadMovie', 'OnInitialized', 'this'  
      &function GetCommandList (      )      
        &pushsdbgv 0							//'commandList'
        &pushone
        &pushsdbgv 1							//'Pointer'
        &pushsdb 2							//'encode'
        &callMethod
        &return
      &end // of function GetCommandList

      &function GetTabHelpSite (      )      
        &pushsdbgv 3							//'tabHelpSite'
        &pushone
        &pushsdbgv 1							//'Pointer'
        &pushsdb 2							//'encode'
        &callMethod
        &return
      &end // of function GetTabHelpSite

      &function2 OnTabPressed () (r:1='this')
        &pushsdb 4							//'FSCommand:'
        &pushsdb 5							//'OnTabPressed'
        &pushregister 1
        &pushbyte 2
        &pushsdb 6							//'qualifyName'
        &callFunction
        &concat
        &pushsdb 7							//''
        &getURL2
      &end // of function OnTabPressed

      &function2 OnTabRollOver () (r:1='this')
        &pushsdb 4							//'FSCommand:'
        &pushsdb 8							//'OnTabRollOver'
        &pushregister 1
        &pushbyte 2
        &pushsdb 6							//'qualifyName'
        &callFunction
        &concat
        &pushsdb 7							//''
        &getURL2
      &end // of function OnTabRollOver

      &function2 OnTabRollOut () (r:1='this')
        &pushsdb 4							//'FSCommand:'
        &pushsdb 9							//'OnTabRollOut'
        &pushregister 1
        &pushbyte 2
        &pushsdb 6							//'qualifyName'
        &callFunction
        &concat
        &pushsdb 7							//''
        &getURL2
      &end // of function OnTabRollOut

      &function onUnload (      )      
        &pushsdb 10							//'GetCommandList'
        &delete2
        &pop
        &pushsdb 11							//'GetTabHelpSite'
        &delete2
        &pop
        &pushsdb 5							//'OnTabPressed'
        &delete2
        &pop
        &pushsdb 8							//'OnTabRollOver'
        &delete2
        &pop
        &pushsdb 9							//'OnTabRollOut'
        &delete2
        &pop
        &pushsdb 12							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 13							//'initialized'
      &not
      &not
      &jnz label1      
      &pushsdb 14							//'disableCommandButtonLoadAnim'
      &pushtrue
      &setVariable
      &pushsdb 15							//'TacticalHUDCommandListBox.swf'
      &pushone
      &pushsdbgv 0							//'commandList'
      &dcallmp 16							// loadMovie()
      &pushsdb 13							//'initialized'
      &pushtrue
      &setVariable
      &pushsdb 4							//'FSCommand:'
      &pushsdb 17							//'OnInitialized'
      &pushthisgv
      &pushbyte 2
      &pushsdb 6							//'qualifyName'
      &callFunction
      &concat
      &pushsdb 7							//''
      &getURL2
     label1:
      &stop
    &end // of frame 0
  &end // of defineMovieClip 75
  
  &exportAssets
    75 &as 'BuildQueuePage'
  &end // of exportAssets

  &frame 0
    &constants 'subTabsInitialized', 'initialized', 'FSCommand:', 'OnInitialized', 'qualifyName', '', 'pages', 'selectedPage', '_visible', 'OnPageSelected', 'OnTabPressed', 'OnTabRollOver', 'OnTabRollOut', 'subTabs', 'SelectTab', 'MakeTabVisible', 'SetTabFlashing', 'length', '_up', 'tabButton', 'gotoAndPlay', 'nextPageId', 'BuildQueuePage', 'attachMovie', '_x', 'pagePos', '_y', 'tabHelpSite', 'subTabHelpSite', '$', 'Text', 'tabIcon', 'InsertTab', 'splice', 'Pointer', 'encode', 'EraseTab', 'SelectPage', 'removeMovieClip', '_disabled', 'mouseOverTab', 'OnTabClicked', 'OnSubTabsInitialized', 'OnSubTabSelected', 'OnSubTabPressed', 'OnSubTabRollOver', 'OnSubTabRollOut', 'InsertPage', 'ErasePage', 'OnSubTabClicked', 'TabHelpSite', 'onUnload', 'this', '_parent', 'OnChildLoaded', 'Array'  
    &function2 OnSubTabsInitialized () (r:1='this')
      &pushsdb 0							//'subTabsInitialized'
      &pushtrue
      &setVariable
      &pushsdbgv 1							//'initialized'
      &not
      &jnz label1      
      &pushsdb 2							//'FSCommand:'
      &pushsdb 3							//'OnInitialized'
      &pushregister 1
      &pushbyte 2
      &pushsdb 4							//'qualifyName'
      &callFunction
      &concat
      &pushsdb 5							//''
      &getURL2
     label1:
    &end // of function OnSubTabsInitialized

    &function2 OnSubTabSelected (r:3='index') (r:1='this')
      &pushregister 3
      &pushzero
      &lessThan
      &not
      &jnz label2      
      &pushundef
      &jmp label3      
     label2:
      &pushsdbgv 6							//'pages'
      &pushregister 3
      &getMember
     label3:
      &setRegister r:2
      &pop
      &pushregister 2
      &pushsdbgv 7							//'selectedPage'
      &equals
      &not
      &not
      &jnz label6      
      &pushsdbgv 7							//'selectedPage'
      &pushundef
      &equals
      &not
      &not
      &jnz label4      
      &pushsdbgv 7							//'selectedPage'
      &pushsdb 8							//'_visible'
      &pushfalse
      &setMember
     label4:
      &pushregister 2
      &pushundef
      &equals
      &not
      &not
      &jnz label5      
      &pushregister 2
      &pushsdb 8							//'_visible'
      &pushtrue
      &setMember
     label5:
      &pushsdb 7							//'selectedPage'
      &pushregister 2
      &setVariable
      &pushsdb 2							//'FSCommand:'
      &pushsdb 9							//'OnPageSelected'
      &pushregister 1
      &pushbyte 2
      &pushsdb 4							//'qualifyName'
      &callFunction
      &concat
      &pushregister 3
      &getURL2
     label6:
    &end // of function OnSubTabSelected

    &function2 OnSubTabPressed (r:1='index') ()
      &pushzero
      &pushsdbgv 6							//'pages'
      &pushregister 1
      &getMember
      &dcallmp 10							// OnTabPressed()
    &end // of function OnSubTabPressed

    &function2 OnSubTabRollOver (r:1='index') ()
      &pushzero
      &pushsdbgv 6							//'pages'
      &pushregister 1
      &getMember
      &dcallmp 11							// OnTabRollOver()
    &end // of function OnSubTabRollOver

    &function2 OnSubTabRollOut (r:1='index') ()
      &pushzero
      &pushsdbgv 6							//'pages'
      &pushregister 1
      &getMember
      &dcallmp 12							// OnTabRollOut()
    &end // of function OnSubTabRollOut

    &function2 SelectPage (r:2='indexArg') ()
      &pushregister 2
      &toNumber
      &setRegister r:1
      &pop
      &pushregister 1
      &pushone
      &pushsdbgv 13							//'subTabs'
      &dcallmp 14							// SelectTab()
      &pushregister 1
      &pushone
      &pushsdbgv 13							//'subTabs'
      &dcallmp 15							// MakeTabVisible()
    &end // of function SelectPage

    &function2 SetTabFlashing (r:3='index', r:2='flashingArg') ()
      &pushregister 2
      &pushzero
      &equals
      &not
      &setRegister r:1
      &pop
      &pushregister 1
      &pushregister 3
      &pushbyte 2
      &pushsdbgv 13							//'subTabs'
      &dcallmp 16							// SetTabFlashing()
    &end // of function SetTabFlashing

    &function2 InsertPage (r:3='index') ()
      &pushsdbgv 6							//'pages'
      &pushsdbgm 17							//'length'
      &pushzero
      &equals
      &not
      &jnz label7      
      &pushsdb 18							//'_up'
      &pushone
      &pushsdbgv 19							//'tabButton'
      &dcallmp 20							// gotoAndPlay()
     label7:
      &pushsdbgv 21							//'nextPageId'
      &pushsdb 21							//'nextPageId'
      &pushsdbgv 21							//'nextPageId'
      &increment
      &setVariable
      &setRegister r:2
      &pop
      &pushregister 2
      &pushregister 2
      &toString
      &pushsdb 22							//'BuildQueuePage'
      &pushbyte 3
      &pushsdb 23							//'attachMovie'
      &callFunction
      &setRegister r:1
      &pop
      &pushregister 1
      &pushsdb 24							//'_x'
      &pushsdbgv 25							//'pagePos'
      &pushsdbgm 24							//'_x'
      &setMember
      &pushregister 1
      &pushsdb 26							//'_y'
      &pushsdbgv 25							//'pagePos'
      &pushsdbgm 26							//'_y'
      &setMember
      &pushregister 1
      &pushsdb 8							//'_visible'
      &pushfalse
      &setMember
      &pushregister 1
      &pushsdb 27							//'tabHelpSite'
      &pushsdbgv 28							//'subTabHelpSite'
      &setMember
      &pushsdb 29							//'$'
      &pushsdb 30							//'Text'
      &pushregister 1
      &pushbyte 2
      &pushsdb 4							//'qualifyName'
      &callFunction
      &add
      &pushsdbgv 31							//'tabIcon'
      &pushregister 3
      &pushbyte 3
      &pushsdbgv 13							//'subTabs'
      &dcallmp 32							// InsertTab()
      &pushregister 1
      &pushzero
      &pushregister 3
      &pushbyte 3
      &pushsdbgv 6							//'pages'
      &dcallmp 33							// splice()
      &pushregister 1
      &pushone
      &pushsdbgv 34							//'Pointer'
      &pushsdb 35							//'encode'
      &callMethod
      &return
    &end // of function InsertPage

    &function2 ErasePage (r:3='index') (r:1='_parent')
      &pushregister 3
      &pushone
      &pushsdbgv 13							//'subTabs'
      &dcallmp 36							// EraseTab()
      &pushsdbgv 6							//'pages'
      &pushregister 3
      &getMember
      &setRegister r:2
      &pop
      &pushregister 2
      &pushsdbgv 7							//'selectedPage'
      &equals
      &not
      &jnz label8      
      &pushundef
      &pushone
      &dcallfp 37							// SelectPage()
     label8:
      &pushzero
      &pushregister 2
      &dcallmp 38							// removeMovieClip()
      &pushone
      &pushregister 3
      &pushbyte 2
      &pushsdbgv 6							//'pages'
      &dcallmp 33							// splice()
      &pushsdbgv 6							//'pages'
      &pushsdbgm 17							//'length'
      &pushzero
      &equals
      &not
      &jnz label10      
      &pushsdb 21							//'nextPageId'
      &pushzerosv
      &pushsdb 5							//''
      &pushbyte 7
      &getProperty
      &not
      &jnz label9      
      &pushzero
      &pushone
      &pushregister 1
      &dcallmp 14							// SelectTab()
     label9:
      &pushsdb 39							//'_disabled'
      &pushone
      &pushsdbgv 19							//'tabButton'
      &dcallmp 20							// gotoAndPlay()
      &pushzero
      &dcallfp 12							// OnTabRollOut()
     label10:
    &end // of function ErasePage

    &function2 OnTabRollOver () (r:1='this')
      &pushsdbgv 40							//'mouseOverTab'
      &not
      &not
      &jnz label11      
      &pushsdb 40							//'mouseOverTab'
      &pushtrue
      &setVariable
      &pushsdb 2							//'FSCommand:'
      &pushsdb 11							//'OnTabRollOver'
      &pushregister 1
      &pushbyte 2
      &pushsdb 4							//'qualifyName'
      &callFunction
      &concat
      &pushsdb 5							//''
      &getURL2
     label11:
    &end // of function OnTabRollOver

    &function2 OnTabRollOut () (r:1='this')
      &pushsdbgv 40							//'mouseOverTab'
      &not
      &jnz label12      
      &pushsdb 40							//'mouseOverTab'
      &pushfalse
      &setVariable
      &pushsdb 2							//'FSCommand:'
      &pushsdb 12							//'OnTabRollOut'
      &pushregister 1
      &pushbyte 2
      &pushsdb 4							//'qualifyName'
      &callFunction
      &concat
      &pushsdb 5							//''
      &getURL2
     label12:
    &end // of function OnTabRollOut

    &function2 OnSubTabClicked (r:2='index') (r:1='this')
      &pushsdb 2							//'FSCommand:'
      &pushsdb 41							//'OnTabClicked'
      &pushregister 1
      &pushbyte 2
      &pushsdb 4							//'qualifyName'
      &callFunction
      &concat
      &pushregister 2
      &toString
      &getURL2
    &end // of function OnSubTabClicked

    &function GetTabHelpSite (    )    
      &pushsdbgv 27							//'tabHelpSite'
      &pushone
      &pushsdbgv 34							//'Pointer'
      &pushsdb 35							//'encode'
      &callMethod
      &return
    &end // of function GetTabHelpSite

    &function onUnload (    )    
      &pushsdb 42							//'OnSubTabsInitialized'
      &delete2
      &pop
      &pushsdb 43							//'OnSubTabSelected'
      &delete2
      &pop
      &pushsdb 44							//'OnSubTabPressed'
      &delete2
      &pop
      &pushsdb 45							//'OnSubTabRollOver'
      &delete2
      &pop
      &pushsdb 46							//'OnSubTabRollOut'
      &delete2
      &pop
      &pushsdb 37							//'SelectPage'
      &delete2
      &pop
      &pushsdb 16							//'SetTabFlashing'
      &delete2
      &pop
      &pushsdb 47							//'InsertPage'
      &delete2
      &pop
      &pushsdb 48							//'ErasePage'
      &delete2
      &pop
      &pushsdb 11							//'OnTabRollOver'
      &delete2
      &pop
      &pushsdb 12							//'OnTabRollOut'
      &delete2
      &pop
      &pushsdb 49							//'OnSubTabClicked'
      &delete2
      &pop
      &pushsdb 50							//'TabHelpSite'
      &delete2
      &pop
      &pushsdb 51							//'onUnload'
      &delete2
      &pop
    &end // of function onUnload

    &pushsdbgv 1							//'initialized'
    &not
    &not
    &jnz label13    
    &pushthisgv
    &pushone
    &pushsdbgv 53							//'_parent'
    &dcallmp 54							// OnChildLoaded()
    &pushsdb 6							//'pages'
    &pushzero
    &pushsdb 55							//'Array'
    &new
    &setVariable
    &pushsdb 21							//'nextPageId'
    &pushzerosv
    &pushsdb 40							//'mouseOverTab'
    &pushfalse
    &setVariable
    &pushsdb 1							//'initialized'
    &pushtrue
    &setVariable
    &pushsdbgv 0							//'subTabsInitialized'
    &not
    &jnz label13    
    &pushsdb 2							//'FSCommand:'
    &pushsdb 3							//'OnInitialized'
    &pushthisgv
    &pushbyte 2
    &pushsdb 4							//'qualifyName'
    &callFunction
    &concat
    &pushsdb 5							//''
    &getURL2
   label13:
    &stop
  &end // of frame 0

  &defineMovieClip 84 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 84
  
  &importAssets &from 'HelpBox.swf'
    'HelpBoxSite' &as 85
  &end // of importAssets

  &placeMovieClip 85 &as 'subTabHelpSite'
  
    &onClipEvent &construct
      &pushs 'vertAlignment'
      &pushssv 'top'
      &pushs 'horzAlignment'
      &pushssv 'right'
    &end
  &end // of placeMovieClip 85

  &defineMovieClip 96 // total frames: 30

    &frame 4
      &stop
    &end // of frame 4

    &frame 9
      &stop
    &end // of frame 9

    &frame 14
      &stop
    &end // of frame 14

    &frame 19
      &stop
    &end // of frame 19

    &frame 24
      &stop
    &end // of frame 24

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 96

  &defineButton 97
  
    &on     &overUpToOverDown
      &gotoLabel '_down'
      &play
    &end
  
    &on     &overDownToOverUp
      &gotoLabel '_release'
      &play
      &pushthisgv
      &pushone
      &pushsgv '_parent'
      &pushs 'OnSpinnerButtonClicked'
      &callmp
    &end
  
    &on     &idleToOverUp    ,&outDownToOverDown    ,&idleToOverDown
      &gotoLabel '_over'
      &play
    &end
  
    &on     &overUpToIdle    ,&overDownToOutDown    ,&overDownToIdle
      &gotoLabel '_up'
      &play
    &end
  &end // of defineButton 97

  &defineMovieClip 104 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 104

  &defineMovieClip 107 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 107

  &defineMovieClip 108 // total frames: 50

    &frame 0
      &constants 'isEnabled', 'SetEnabled', 'onUnload', 'initialized'  
      &function2 SetEnabled (r:1='enable') ()
        &pushregister 1
        &pushsdbgv 0							//'isEnabled'
        &equals
        &not
        &not
        &jnz label3        
        &pushregister 1
        &not
        &jnz label1        
        &gotoLabel '_up'
        &play
        &jmp label2        
       label1:
        &gotoLabel '_disabled'
        &play
       label2:
        &pushsdb 0							//'isEnabled'
        &pushregister 1
        &setVariable
       label3:
      &end // of function SetEnabled

      &function onUnload (      )      
        &pushsdb 1							//'SetEnabled'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'initialized'
      &not
      &not
      &jnz label5      
      &pushsdbgv 0							//'isEnabled'
      &not
      &not
      &jnz label4      
      &gotoLabel '_disabled'
      &play
     label4:
      &pushsdb 3							//'initialized'
      &pushtrue
      &setVariable
     label5:
    &end // of frame 0

    &frame 8
      &stop
    &end // of frame 8

    &frame 18
      &stop
    &end // of frame 18

    &frame 28
      &stop
    &end // of frame 28

    &frame 38
      &gotoLabel '_up'
      &play
    &end // of frame 38

    &frame 49
      &stop
    &end // of frame 49
  &end // of defineMovieClip 108

  &defineButton 109
  
    &on     &overUpToOverDown
      &gotoLabel '_down'
      &play
    &end
  
    &on     &overDownToOverUp
      &gotoLabel '_release'
      &play
      &pushthisgv
      &pushone
      &pushsgv '_parent'
      &pushs 'OnSpinnerButtonClicked'
      &callmp
    &end
  
    &on     &idleToOverUp    ,&outDownToOverDown    ,&idleToOverDown
      &gotoLabel '_over'
      &play
    &end
  
    &on     &overUpToIdle    ,&overDownToOutDown    ,&overDownToIdle
      &gotoLabel '_up'
      &play
    &end
  &end // of defineButton 109

  &defineMovieClip 116 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 116

  &defineMovieClip 119 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'factionSkinned', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &pushregister 1
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &pushregister 1
        &pushone
        &pushregister 2
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'factionSkinned'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'factionSkinned'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 119

  &defineMovieClip 120 // total frames: 50

    &frame 0
      &constants 'isEnabled', 'SetEnabled', 'onUnload', 'initialized'  
      &function2 SetEnabled (r:1='enable') ()
        &pushregister 1
        &pushsdbgv 0							//'isEnabled'
        &equals
        &not
        &not
        &jnz label3        
        &pushregister 1
        &not
        &jnz label1        
        &gotoLabel '_up'
        &play
        &jmp label2        
       label1:
        &gotoLabel '_disabled'
        &play
       label2:
        &pushsdb 0							//'isEnabled'
        &pushregister 1
        &setVariable
       label3:
      &end // of function SetEnabled

      &function onUnload (      )      
        &pushsdb 1							//'SetEnabled'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'initialized'
      &not
      &not
      &jnz label5      
      &pushsdbgv 0							//'isEnabled'
      &not
      &not
      &jnz label4      
      &gotoLabel '_disabled'
      &play
     label4:
      &pushsdb 3							//'initialized'
      &pushtrue
      &setVariable
     label5:
    &end // of frame 0

    &frame 8
      &stop
    &end // of frame 8

    &frame 18
      &stop
    &end // of frame 18

    &frame 28
      &stop
    &end // of frame 28

    &frame 38
      &gotoLabel '_up'
      &play
    &end // of frame 38

    &frame 49
      &stop
    &end // of frame 49
  &end // of defineMovieClip 120

  &defineMovieClip 121 // total frames: 1

    &frame 0
      &constants 'tabButtons', 'length', 'selectedTabButton', '_up', 'gotoAndPlay', '_selected', 'GetTabButtonIndex', 'client', 'OnSubTabSelected', 'OutlineSelectedTab', 'tabScrollPos', 'numVisibleTabs', '_', 'tabOutline', '_none', 'SelectTabButton', '_off', '_on', 'flashClip', 'OnSubTabPressed', 'OnSubTabClicked', 'OnSubTabRollOver', 'OnSubTabRollOut', 'tabSlotWidth', 'buttons', '_x', 'buttonStageLeft', '_visible', 'ShouldTabButtonBeVisible', 'UpdateTabButtonVisibility', 'CanScrollLeft', 'spinLeftButton', 'SetSpinnerButtonEnabled', 'CanScrollRight', 'spinRightButton', 'nextTabButtonId', 'TabButton', 'attachMovie', 'iconLabel', 'text', 'splice', 'removeMovieClip', 'ScrollTo', 'initialized', 'SetEnabled', 'isEnabled', 'SelectTab', 'SetTabFlashing', 'GetSelectedTabNum', 'OnPressed', 'OnClicked', 'OnRollOver', 'OnRollOut', 'InsertTab', 'EraseTab', 'OnSpinnerButtonClicked', 'MakeTabVisible', 'onUnload', 'extern', 'InGame', '_root', 'GetCurrentFaction', 'Alien', '_parent', 'Array', 'this', 'OnSubTabsInitialized'  
      &function2 GetTabButtonIndex (r:2='tabButton') ()
        &pushregister 2
        &pushundef
        &equals
        &not
        &jnz label1        
        &pushbyte -1
        &return
       label1:
        &pushzero
        &setRegister r:1
        &pop
       label2:
        &pushregister 1
        &pushsdbgv 0							//'tabButtons'
        &pushsdbgm 1							//'length'
        &lessThan
        &not
        &jnz label4        
        &pushregister 2
        &pushsdbgv 0							//'tabButtons'
        &pushregister 1
        &getMember
        &equals
        &not
        &jnz label3        
        &pushregister 1
        &return
       label3:
        &pushregister 1
        &increment
        &setRegister r:1
        &pop
        &jmp label2        
       label4:
        &pushbyte -1
        &return
      &end // of function GetTabButtonIndex

      &function2 SelectTabButton (r:1='tabButton') ()
        &pushregister 1
        &pushsdbgv 2							//'selectedTabButton'
        &equals
        &not
        &not
        &jnz label7        
        &pushsdbgv 2							//'selectedTabButton'
        &pushundef
        &equals
        &not
        &not
        &jnz label5        
        &pushsdb 3							//'_up'
        &pushone
        &pushsdbgv 2							//'selectedTabButton'
        &dcallmp 4							// gotoAndPlay()
       label5:
        &pushregister 1
        &pushundef
        &equals
        &not
        &not
        &jnz label6        
        &pushsdb 5							//'_selected'
        &pushone
        &pushregister 1
        &dcallmp 4							// gotoAndPlay()
       label6:
        &pushsdb 2							//'selectedTabButton'
        &pushregister 1
        &setVariable
        &pushsdbgv 2							//'selectedTabButton'
        &pushone
        &pushsdb 6							//'GetTabButtonIndex'
        &callFunction
        &pushone
        &pushsdbgv 7							//'client'
        &dcallmp 8							// OnSubTabSelected()
        &pushzero
        &dcallfp 9							// OutlineSelectedTab()
       label7:
      &end // of function SelectTabButton

      &function2 OutlineSelectedTab () ()
        &pushsdbgv 2							//'selectedTabButton'
        &pushone
        &pushsdb 6							//'GetTabButtonIndex'
        &callFunction
        &pushsdbgv 10							//'tabScrollPos'
        &subtract
        &setRegister r:1
        &pop
        &pushregister 1
        &pushzero
        &lessThan
        &not
        &dup
        &not
        &jnz label8        
        &pop
        &pushregister 1
        &pushsdbgv 11							//'numVisibleTabs'
        &lessThan
       label8:
        &not
        &jnz label9        
        &pushsdb 12							//'_'
        &pushregister 1
        &toString
        &add
        &pushone
        &pushsdbgv 13							//'tabOutline'
        &dcallmp 4							// gotoAndPlay()
        &jmp label10        
       label9:
        &pushsdb 14							//'_none'
        &pushone
        &pushsdbgv 13							//'tabOutline'
        &dcallmp 4							// gotoAndPlay()
       label10:
      &end // of function OutlineSelectedTab

      &function2 SelectTab (r:1='index') ()
        &pushsdbgv 0							//'tabButtons'
        &pushregister 1
        &getMember
        &pushone
        &dcallfp 15							// SelectTabButton()
      &end // of function SelectTab

      &function2 SetTabFlashing (r:1='index', r:2='flashing') ()
        &pushregister 2
        &jnz label11        
        &pushsdb 16							//'_off'
        &jmp label12        
       label11:
        &pushsdb 17							//'_on'
       label12:
        &pushone
        &pushsdbgv 0							//'tabButtons'
        &pushregister 1
        &getMember
        &pushsdbgm 18							//'flashClip'
        &dcallmp 4							// gotoAndPlay()
      &end // of function SetTabFlashing

      &function GetSelectedTabNum (      )      
        &pushsdbgv 2							//'selectedTabButton'
        &pushone
        &pushsdb 6							//'GetTabButtonIndex'
        &callFunction
        &return
      &end // of function GetSelectedTabNum

      &function2 OnPressed (r:1='buttonClip') ()
        &pushregister 1
        &pushone
        &pushsdb 6							//'GetTabButtonIndex'
        &callFunction
        &pushone
        &pushsdbgv 7							//'client'
        &dcallmp 19							// OnSubTabPressed()
      &end // of function OnPressed

      &function2 OnClicked (r:1='buttonClip') ()
        &pushregister 1
        &pushone
        &pushsdb 6							//'GetTabButtonIndex'
        &callFunction
        &pushone
        &pushsdbgv 7							//'client'
        &dcallmp 20							// OnSubTabClicked()
        &pushregister 1
        &pushone
        &dcallfp 15							// SelectTabButton()
      &end // of function OnClicked

      &function2 OnRollOver (r:1='buttonClip') ()
        &pushregister 1
        &pushone
        &pushsdb 6							//'GetTabButtonIndex'
        &callFunction
        &pushone
        &pushsdbgv 7							//'client'
        &dcallmp 21							// OnSubTabRollOver()
      &end // of function OnRollOver

      &function2 OnRollOut (r:1='buttonClip') ()
        &pushregister 1
        &pushone
        &pushsdb 6							//'GetTabButtonIndex'
        &callFunction
        &pushone
        &pushsdbgv 7							//'client'
        &dcallmp 22							// OnSubTabRollOut()
      &end // of function OnRollOut

      &function2 ShouldTabButtonBeVisible (r:3='tabButton') ()
        &pushzero
        &pushsdbgv 23							//'tabSlotWidth'
        &subtract
        &pushsdbgv 24							//'buttons'
        &pushsdbgm 25							//'_x'
        &pushsdbgv 26							//'buttonStageLeft'
        &subtract
        &subtract
        &setRegister r:2
        &pop
        &pushsdbgv 23							//'tabSlotWidth'
        &pushsdbgv 11							//'numVisibleTabs'
        &multiply
        &pushsdbgv 24							//'buttons'
        &pushsdbgm 25							//'_x'
        &pushsdbgv 26							//'buttonStageLeft'
        &subtract
        &subtract
        &setRegister r:1
        &pop
        &pushregister 3
        &pushsdbgm 25							//'_x'
        &pushregister 2
        &greaterThan
        &dup
        &not
        &jnz label13        
        &pop
        &pushregister 3
        &pushsdbgm 25							//'_x'
        &pushregister 1
        &lessThan
       label13:
        &return
      &end // of function ShouldTabButtonBeVisible

      &function2 UpdateTabButtonVisibility () ()
        &pushzero
        &setRegister r:1
        &pop
       label14:
        &pushregister 1
        &pushsdbgv 0							//'tabButtons'
        &pushsdbgm 1							//'length'
        &lessThan
        &not
        &jnz label15        
        &pushsdbgv 0							//'tabButtons'
        &pushregister 1
        &getMember
        &pushsdb 27							//'_visible'
        &pushsdbgv 0							//'tabButtons'
        &pushregister 1
        &getMember
        &pushone
        &pushsdb 28							//'ShouldTabButtonBeVisible'
        &callFunction
        &setMember
        &pushregister 1
        &increment
        &setRegister r:1
        &pop
        &jmp label14        
       label15:
        &pushzero
        &dcallfp 9							// OutlineSelectedTab()
      &end // of function UpdateTabButtonVisibility

      &function2 ScrollTo (r:1='index') ()
        &pushsdbgv 24							//'buttons'
        &pushsdb 25							//'_x'
        &pushsdbgv 26							//'buttonStageLeft'
        &pushregister 1
        &pushsdbgv 23							//'tabSlotWidth'
        &multiply
        &subtract
        &setMember
        &pushsdb 10							//'tabScrollPos'
        &pushregister 1
        &setVariable
        &pushzero
        &dcallfp 29							// UpdateTabButtonVisibility()
        &pushzero
        &pushsdb 30							//'CanScrollLeft'
        &callFunction
        &pushsdbgv 31							//'spinLeftButton'
        &pushbyte 2
        &dcallfp 32							// SetSpinnerButtonEnabled()
        &pushzero
        &pushsdb 33							//'CanScrollRight'
        &callFunction
        &pushsdbgv 34							//'spinRightButton'
        &pushbyte 2
        &dcallfp 32							// SetSpinnerButtonEnabled()
      &end // of function ScrollTo

      &function2 InsertTab (r:3='index', r:7='iconLabel', r:8='tabText') (r:1='this')
        &pushregister 3
        &pushsdbgv 23							//'tabSlotWidth'
        &multiply
        &setRegister r:4
        &pop
        &pushsdbgv 35							//'nextTabButtonId'
        &pushsdb 35							//'nextTabButtonId'
        &pushsdbgv 35							//'nextTabButtonId'
        &increment
        &setVariable
        &setRegister r:6
        &pop
        &pushregister 6
        &pushregister 6
        &toString
        &pushsdb 36							//'TabButton'
        &pushbyte 3
        &pushsdbgv 24							//'buttons'
        &pushsdb 37							//'attachMovie'
        &callMethod
        &setRegister r:5
        &pop
        &pushregister 5
        &pushsdb 25							//'_x'
        &pushregister 4
        &setMember
        &pushregister 5
        &pushsdb 27							//'_visible'
        &pushregister 5
        &pushone
        &pushsdb 28							//'ShouldTabButtonBeVisible'
        &callFunction
        &setMember
        &pushregister 5
        &pushsdb 38							//'iconLabel'
        &pushregister 7
        &setMember
        &pushregister 5
        &pushsdb 39							//'text'
        &pushregister 8
        &setMember
        &pushregister 5
        &pushsdb 7							//'client'
        &pushregister 1
        &setMember
        &pushregister 5
        &pushzero
        &pushregister 3
        &pushbyte 3
        &pushsdbgv 0							//'tabButtons'
        &dcallmp 40							// splice()
       label16:
        &pushfalse
        &jnz label18        
        &pushregister 3
        &increment
        &setRegister r:3
        &pop
        &pushregister 3
        &pushsdbgv 0							//'tabButtons'
        &pushsdbgm 1							//'length'
        &lessThan
        &not
        &not
        &jnz label17        
        &jmp label18        
       label17:
        &pushregister 4
        &pushsdbgv 23							//'tabSlotWidth'
        &add
        &setRegister r:4
        &pop
        &pushsdbgv 0							//'tabButtons'
        &pushregister 3
        &getMember
        &setRegister r:2
        &pop
        &pushregister 2
        &pushsdb 25							//'_x'
        &pushregister 4
        &setMember
        &pushregister 2
        &pushsdb 27							//'_visible'
        &pushregister 2
        &pushone
        &pushsdb 28							//'ShouldTabButtonBeVisible'
        &callFunction
        &setMember
        &jmp label16        
       label18:
        &pushzero
        &pushsdb 33							//'CanScrollRight'
        &callFunction
        &pushsdbgv 34							//'spinRightButton'
        &pushbyte 2
        &dcallfp 32							// SetSpinnerButtonEnabled()
      &end // of function InsertTab

      &function2 EraseTab (r:2='index') ()
        &pushsdbgv 0							//'tabButtons'
        &pushregister 2
        &getMember
        &setRegister r:5
        &pop
        &pushregister 5
        &pushsdbgm 25							//'_x'
        &setRegister r:3
        &pop
        &pushsdbgv 2							//'selectedTabButton'
        &pushregister 5
        &equals
        &not
        &jnz label19        
        &pushundef
        &pushone
        &dcallfp 15							// SelectTabButton()
       label19:
        &pushzero
        &pushregister 5
        &dcallmp 41							// removeMovieClip()
        &pushone
        &pushregister 2
        &pushbyte 2
        &pushsdbgv 0							//'tabButtons'
        &dcallmp 40							// splice()
        &pushregister 2
        &pushsdbgv 0							//'tabButtons'
        &pushsdbgm 1							//'length'
        &lessThan
        &not
        &jnz label22        
       label20:
        &pushfalse
        &jnz label22        
        &pushsdbgv 0							//'tabButtons'
        &pushregister 2
        &getMember
        &setRegister r:1
        &pop
        &pushregister 1
        &pushsdb 25							//'_x'
        &pushregister 3
        &setMember
        &pushregister 1
        &pushsdb 27							//'_visible'
        &pushregister 1
        &pushone
        &pushsdb 28							//'ShouldTabButtonBeVisible'
        &callFunction
        &setMember
        &pushregister 2
        &increment
        &setRegister r:2
        &pop
        &pushregister 2
        &pushsdbgv 0							//'tabButtons'
        &pushsdbgm 1							//'length'
        &lessThan
        &not
        &not
        &jnz label21        
        &jmp label22        
       label21:
        &pushregister 3
        &pushsdbgv 23							//'tabSlotWidth'
        &add
        &setRegister r:3
        &pop
        &jmp label20        
       label22:
        &pushsdbgv 0							//'tabButtons'
        &pushsdbgm 1							//'length'
        &pushzero
        &equals
        &not
        &jnz label23        
        &pushsdb 35							//'nextTabButtonId'
        &pushzerosv
       label23:
        &pushsdbgv 10							//'tabScrollPos'
        &setRegister r:4
        &pop
        &pushregister 4
        &pushsdbgv 0							//'tabButtons'
        &pushsdbgm 1							//'length'
        &pushsdbgv 11							//'numVisibleTabs'
        &subtract
        &greaterThan
        &not
        &jnz label24        
        &pushsdbgv 0							//'tabButtons'
        &pushsdbgm 1							//'length'
        &pushsdbgv 11							//'numVisibleTabs'
        &subtract
        &setRegister r:4
        &pop
       label24:
        &pushregister 4
        &pushzero
        &lessThan
        &not
        &jnz label25        
        &pushzero
        &setRegister r:4
        &pop
       label25:
        &pushregister 4
        &pushsdbgv 10							//'tabScrollPos'
        &equals
        &not
        &not
        &jnz label26        
        &pushregister 4
        &pushone
        &dcallfp 42							// ScrollTo()
       label26:
      &end // of function EraseTab

      &function CanScrollLeft (      )      
        &pushsdbgv 10							//'tabScrollPos'
        &pushzero
        &greaterThan
        &return
      &end // of function CanScrollLeft

      &function CanScrollRight (      )      
        &pushsdbgv 10							//'tabScrollPos'
        &pushsdbgv 0							//'tabButtons'
        &pushsdbgm 1							//'length'
        &pushsdbgv 11							//'numVisibleTabs'
        &subtract
        &lessThan
        &return
      &end // of function CanScrollRight

      &function2 SetSpinnerButtonEnabled (r:1='buttonClip', r:2='enable') ()
        &pushregister 1
        &pushsdbgm 43							//'initialized'
        &not
        &jnz label27        
        &pushregister 2
        &pushone
        &pushregister 1
        &dcallmp 44							// SetEnabled()
        &jmp label28        
       label27:
        &pushregister 1
        &pushsdb 45							//'isEnabled'
        &pushregister 2
        &setMember
       label28:
      &end // of function SetSpinnerButtonEnabled

      &function2 OnSpinnerButtonClicked (r:1='buttonClip') ()
        &pushregister 1
        &pushsdbgv 31							//'spinLeftButton'
        &equals
        &not
        &jnz label30        
        &pushzero
        &pushsdb 30							//'CanScrollLeft'
        &callFunction
        &not
        &jnz label29        
        &pushsdbgv 10							//'tabScrollPos'
        &pushone
        &subtract
        &pushone
        &dcallfp 42							// ScrollTo()
       label29:
        &jmp label31        
       label30:
        &pushzero
        &pushsdb 33							//'CanScrollRight'
        &callFunction
        &not
        &jnz label31        
        &pushsdbgv 10							//'tabScrollPos'
        &pushone
        &add
        &pushone
        &dcallfp 42							// ScrollTo()
       label31:
      &end // of function OnSpinnerButtonClicked

      &function2 MakeTabVisible (r:1='index') ()
        &pushregister 1
        &pushsdbgv 10							//'tabScrollPos'
        &lessThan
        &not
        &jnz label32        
        &pushregister 1
        &pushone
        &dcallfp 42							// ScrollTo()
        &jmp label33        
       label32:
        &pushregister 1
        &pushsdbgv 10							//'tabScrollPos'
        &pushsdbgv 11							//'numVisibleTabs'
        &add
        &lessThan
        &not
        &not
        &jnz label33        
        &pushregister 1
        &pushsdbgv 11							//'numVisibleTabs'
        &subtract
        &pushone
        &add
        &pushone
        &dcallfp 42							// ScrollTo()
       label33:
      &end // of function MakeTabVisible

      &function onUnload (      )      
        &pushsdb 6							//'GetTabButtonIndex'
        &delete2
        &pop
        &pushsdb 15							//'SelectTabButton'
        &delete2
        &pop
        &pushsdb 9							//'OutlineSelectedTab'
        &delete2
        &pop
        &pushsdb 46							//'SelectTab'
        &delete2
        &pop
        &pushsdb 47							//'SetTabFlashing'
        &delete2
        &pop
        &pushsdb 48							//'GetSelectedTabNum'
        &delete2
        &pop
        &pushsdb 49							//'OnPressed'
        &delete2
        &pop
        &pushsdb 50							//'OnClicked'
        &delete2
        &pop
        &pushsdb 51							//'OnRollOver'
        &delete2
        &pop
        &pushsdb 52							//'OnRollOut'
        &delete2
        &pop
        &pushsdb 28							//'ShouldTabButtonBeVisible'
        &delete2
        &pop
        &pushsdb 29							//'UpdateTabButtonVisibility'
        &delete2
        &pop
        &pushsdb 42							//'ScrollTo'
        &delete2
        &pop
        &pushsdb 53							//'InsertTab'
        &delete2
        &pop
        &pushsdb 54							//'EraseTab'
        &delete2
        &pop
        &pushsdb 30							//'CanScrollLeft'
        &delete2
        &pop
        &pushsdb 33							//'CanScrollRight'
        &delete2
        &pop
        &pushsdb 32							//'SetSpinnerButtonEnabled'
        &delete2
        &pop
        &pushsdb 55							//'OnSpinnerButtonClicked'
        &delete2
        &pop
        &pushsdb 56							//'MakeTabVisible'
        &delete2
        &pop
        &pushsdb 57							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 43							//'initialized'
      &not
      &not
      &jnz label36      
      &pushsdbgv 58							//'extern'
      &pushsdbgm 59							//'InGame'
      &not
      &not
      &jnz label34      
      &pushsdbgv 60							//'_root'
      &pushsdb 61							//'GetCurrentFaction'
      &function  (      )      
        &pushsdb 62							//'Alien'
        &return
      &end // of function 

      &setMember
     label34:
      &pushsdb 23							//'tabSlotWidth'
      &pushbyte 29
      &setVariable
      &pushsdb 11							//'numVisibleTabs'
      &pushbyte 5
      &setVariable
      &pushsdb 26							//'buttonStageLeft'
      &pushsdbgv 24							//'buttons'
      &pushsdbgm 25							//'_x'
      &setVariable
      &pushsdb 10							//'tabScrollPos'
      &pushzerosv
      &pushsdbgv 7							//'client'
      &pushundef
      &equals
      &not
      &jnz label35      
      &pushsdb 7							//'client'
      &pushsdbgv 63							//'_parent'
      &setVariable
     label35:
      &pushsdb 0							//'tabButtons'
      &pushzero
      &pushsdb 64							//'Array'
      &new
      &setVariable
      &pushsdb 35							//'nextTabButtonId'
      &pushzerosv
      &pushfalse
      &pushsdbgv 31							//'spinLeftButton'
      &pushbyte 2
      &dcallfp 32							// SetSpinnerButtonEnabled()
      &pushfalse
      &pushsdbgv 34							//'spinRightButton'
      &pushbyte 2
      &dcallfp 32							// SetSpinnerButtonEnabled()
      &pushsdb 43							//'initialized'
      &pushtrue
      &setVariable
      &pushthisgv
      &pushone
      &pushsdbgv 7							//'client'
      &dcallmp 66							// OnSubTabsInitialized()
     label36:
    &end // of frame 0
  &end // of defineMovieClip 121
&end
