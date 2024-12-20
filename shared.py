import audio
mouse_states=['character_selected','item_selected','spawning','free']
mouse_current_state='free'
mouse_down=False
mouse_pos=(0,0)
screen=None
selected_character=None
player_audio_source=audio.AudioSource(0)
player_audio_source.add_sound('click','Sounds\click.wav')
player_audio_source.add_sound('select','Sounds\select.wav')
player_audio_source.add_sound('hover','Sounds\hover.wav')