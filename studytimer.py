import time
import json
import os
from datetime import datetime
from playsound import playsound
import threading

class StudyTimer:
    def __init__(self):
        self.sessions_file = 'study_sessions.json'
        self.work_duration = 25 * 60  # 25 minutes in seconds
        self.short_break = 5 * 60     # 5 minutes
        self.long_break = 15 * 60     # 15 minutes
        self.sessions_until_long_break = 4
        self.current_session = 0
        self.total_sessions_today = 0
        self.is_running = False
        
    def load_sessions(self):
        """Load previous study sessions from file"""
        if os.path.exists(self.sessions_file):
            with open(self.sessions_file, 'r') as f:
                return json.load(f)
        return []
    
    def save_session(self, session_type, duration):
        """Save completed session to history"""
        sessions = self.load_sessions()
        session = {
            'type': session_type,
            'duration': duration,
            'timestamp': datetime.now().isoformat(),
            'date': datetime.now().strftime('%Y-%m-%d')
        }
        sessions.append(session)
        
        with open(self.sessions_file, 'w') as f:
            json.dump(sessions, f, indent=2)
    
    def get_today_stats(self):
        """Calculate statistics for today's sessions"""
        sessions = self.load_sessions()
        today = datetime.now().strftime('%Y-%m-%d')
        today_sessions = [s for s in sessions if s.get('date') == today and s['type'] == 'work']
        
        total_minutes = sum(s['duration'] for s in today_sessions) // 60
        return len(today_sessions), total_minutes
    
    def play_notification(self):
        """Play a simple beep notification (using system bell if playsound unavailable)"""
        try:
            # If you have an audio file, you can use it here
            # playsound('notification.mp3')
            print('\a')  # System bell
        except:
            print('\a')
    
    def format_time(self, seconds):
        """Format seconds into MM:SS"""
        mins = seconds // 60
        secs = seconds % 60
        return f"{mins:02d}:{secs:02d}"
    
    def countdown(self, duration, session_type):
        """Run countdown timer with live display"""
        self.is_running = True
        start_time = time.time()
        end_time = start_time + duration
        
        print(f"\n{'='*50}")
        print(f"🎯 {session_type.upper()} SESSION STARTED")
        print(f"Duration: {self.format_time(duration)}")
        print(f"{'='*50}\n")
        
        try:
            while time.time() < end_time and self.is_running:
                remaining = int(end_time - time.time())
                
                # Create progress bar
                progress = 1 - (remaining / duration)
                bar_length = 30
                filled = int(bar_length * progress)
                bar = '█' * filled + '░' * (bar_length - filled)
                
                # Display timer
                print(f"\r⏱️  {self.format_time(remaining)} [{bar}] {int(progress*100)}%", end='', flush=True)
                time.sleep(1)
            
            if self.is_running:
                print(f"\n\n✅ {session_type.upper()} SESSION COMPLETE!\n")
                self.play_notification()
                self.save_session(session_type, duration)
                return True
            else:
                print(f"\n\n⏸️  {session_type.upper()} SESSION PAUSED\n")
                return False
                
        except KeyboardInterrupt:
            print(f"\n\n⏸️  {session_type.upper()} SESSION INTERRUPTED\n")
            self.is_running = False
            return False
    
    def start_work_session(self):
        """Start a work/study session"""
        self.current_session += 1
        completed = self.countdown(self.work_duration, 'work')
        
        if completed:
            self.total_sessions_today += 1
            return True
        return False
    
    def start_break(self):
        """Start appropriate break based on session count"""
        if self.current_session % self.sessions_until_long_break == 0:
            print("🌟 Time for a LONG BREAK! Stretch, walk around, rest your eyes.")
            self.countdown(self.long_break, 'long break')
        else:
            print("☕ Time for a SHORT BREAK! Step away from your work.")
            self.countdown(self.short_break, 'short break')
    
    def show_stats(self):
        """Display today's statistics"""
        sessions, minutes = self.get_today_stats()
        print(f"\n{'='*50}")
        print(f"📊 TODAY'S STUDY STATISTICS")
        print(f"{'='*50}")
        print(f"Sessions completed: {sessions}")
        print(f"Total study time: {minutes} minutes ({minutes/60:.1f} hours)")
        print(f"{'='*50}\n")
    
    def customize_settings(self):
        """Allow user to customize timer settings"""
        print("\n⚙️  CUSTOMIZE SETTINGS")
        print(f"Current work duration: {self.work_duration//60} minutes")
        print(f"Current short break: {self.short_break//60} minutes")
        print(f"Current long break: {self.long_break//60} minutes")
        print(f"Sessions until long break: {self.sessions_until_long_break}")
        
        try:
            work = input("\nWork duration (minutes, press Enter to keep current): ")
            if work:
                self.work_duration = int(work) * 60
            
            short = input("Short break (minutes, press Enter to keep current): ")
            if short:
                self.short_break = int(short) * 60
            
            long = input("Long break (minutes, press Enter to keep current): ")
            if long:
                self.long_break = int(long) * 60
            
            sessions = input("Sessions until long break (press Enter to keep current): ")
            if sessions:
                self.sessions_until_long_break = int(sessions)
            
            print("\n✅ Settings updated!")
        except ValueError:
            print("\n❌ Invalid input. Settings unchanged.")
    
    def run(self):
        """Main application loop"""
        print("\n" + "="*50)
        print("🎓 STUDY TIMER - FOCUS SESSION MANAGER")
        print("="*50)
        
        while True:
            self.show_stats()
            print("\nOptions:")
            print("1. Start work session")
            print("2. Start break")
            print("3. View statistics")
            print("4. Customize settings")
            print("5. Exit")
            
            choice = input("\nSelect option (1-5): ").strip()
            
            if choice == '1':
                if self.start_work_session():
                    auto_break = input("\nStart break automatically? (y/n): ").lower()
                    if auto_break == 'y':
                        self.start_break()
            
            elif choice == '2':
                self.start_break()
            
            elif choice == '3':
                self.show_stats()
                input("\nPress Enter to continue...")
            
            elif choice == '4':
                self.customize_settings()
            
            elif choice == '5':
                print("\n👋 Great work today! Keep up the focus!\n")
                break
            
            else:
                print("\n❌ Invalid option. Please try again.")

if __name__ == "__main__":
    timer = StudyTimer()
    timer.run()