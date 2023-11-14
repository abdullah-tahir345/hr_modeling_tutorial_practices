class Television:
    def __init__(self, display, sound):
        self.display = display
        self.sound = sound
        
    def turn_on(self):
        self.display = 'ON'
        return self.display
        
    def turn_off(self):
        self.display = 'OFF'
        return self.display
        
    def change_channel(self):
        print('Channal Changed')
        

class SmartSpeaker:
    def __init__(self, audio_output, voice_assistant):
        self.audio_output = audio_output
        self.voice_assistant = voice_assistant
        
    def play_music(self):
        self.audio_output = 'ON'
        return self.audio_output
        
    def stop_music(self):
        self.audio_output = 'OFF'
        return self.audio_output
        
    def activate_voice_assistant(self):
        self.voice_assistant = 'ON'
        return self.voice_assistant
        
        
class SmartTV(Television, SmartSpeaker):
    def __init__(self, display, sound):
        Television.__init__(self, display, sound)
        SmartSpeaker.__init__(self, 'OFF', 'OFF')
        
        
s = SmartTV('VGA', 'OFF')
print(s.turn_on())
print(s.turn_off())

print()
print(s.play_music())
print(s.stop_music())