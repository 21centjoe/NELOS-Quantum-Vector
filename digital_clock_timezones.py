"""
Digital Clock with Multiple Time Zone Display
Displays current time in different time zones with real-time updates
"""

from datetime import datetime
import pytz
from typing import List, Dict
import os
import sys

class DigitalClock:
    """A digital clock that displays time in multiple time zones."""
    
    def __init__(self, timezones: List[str] = None):
        """
        Initialize the digital clock with specified time zones.
        
        Args:
            timezones: List of timezone strings (e.g., ['US/Eastern', 'Europe/London'])
                      If None, uses default major cities' timezones
        """
        self.timezones = timezones or [
            'US/Eastern',
            'US/Central',
            'US/Mountain',
            'US/Pacific',
            'Europe/London',
            'Europe/Paris',
            'Asia/Tokyo',
            'Australia/Sydney',
            'UTC'
        ]
        
        # Friendly names for timezones
        self.timezone_names = {
            'US/Eastern': 'New York (EST)',
            'US/Central': 'Chicago (CST)',
            'US/Mountain': 'Denver (MST)',
            'US/Pacific': 'Los Angeles (PST)',
            'Europe/London': 'London (GMT)',
            'Europe/Paris': 'Paris (CET)',
            'Asia/Tokyo': 'Tokyo (JST)',
            'Australia/Sydney': 'Sydney (AEDT)',
            'UTC': 'UTC'
        }
    
    def get_time_in_timezone(self, tz_name: str) -> datetime:
        """
        Get current time in specified timezone.
        
        Args:
            tz_name: Timezone string (e.g., 'US/Eastern')
            
        Returns:
            datetime object in the specified timezone
        """
        try:
            tz = pytz.timezone(tz_name)
            return datetime.now(tz)
        except pytz.exceptions.UnknownTimeZoneError:
            print(f"Error: Unknown timezone '{tz_name}'")
            return None
    
    def format_time(self, dt: datetime, include_date: bool = False, 
                   include_seconds: bool = True) -> str:
        """
        Format datetime object as a readable string.
        
        Args:
            dt: datetime object to format
            include_date: Whether to include the date
            include_seconds: Whether to include seconds
            
        Returns:
            Formatted time string
        """
        if include_seconds:
            time_format = "%H:%M:%S"
        else:
            time_format = "%H:%M"
        
        result = dt.strftime(time_format)
        
        if include_date:
            result = dt.strftime("%A, %B %d, %Y") + " | " + result
        
        return result
    
    def display_clock(self, include_date: bool = False, include_seconds: bool = True):
        """
        Display the digital clock for all configured timezones.
        
        Args:
            include_date: Whether to include the date
            include_seconds: Whether to include seconds
        """
        self._clear_screen()
        
        print("=" * 70)
        print(" " * 15 + "DIGITAL CLOCK - WORLD TIME ZONES")
        print("=" * 70)
        print()
        
        for tz in self.timezones:
            dt = self.get_time_in_timezone(tz)
            if dt:
                friendly_name = self.timezone_names.get(tz, tz)
                time_str = self.format_time(dt, include_date, include_seconds)
                
                # Format output with alignment
                print(f"  {friendly_name:.<30} {time_str}")
        
        print()
        print("=" * 70)
        print("Press Ctrl+C to stop | Updates every second")
        print("=" * 70)
    
    def _clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def run_continuous(self, include_date: bool = False, include_seconds: bool = True):
        """
        Run the clock continuously, updating every second.
        
        Args:
            include_date: Whether to include the date
            include_seconds: Whether to include seconds
        """
        import time
        
        try:
            while True:
                self.display_clock(include_date, include_seconds)
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\nClock stopped. Goodbye!")
            sys.exit(0)
    
    def get_all_times(self) -> Dict[str, str]:
        """
        Get all current times as a dictionary.
        
        Returns:
            Dictionary with timezone names as keys and formatted times as values
        """
        times = {}
        for tz in self.timezones:
            dt = self.get_time_in_timezone(tz)
            if dt:
                friendly_name = self.timezone_names.get(tz, tz)
                times[friendly_name] = self.format_time(dt)
        return times
    
    def add_timezone(self, tz_name: str, friendly_name: str = None):
        """
        Add a new timezone to the clock.
        
        Args:
            tz_name: Timezone string (e.g., 'Asia/Bangkok')
            friendly_name: Display name for the timezone (optional)
        """
        if tz_name not in self.timezones:
            self.timezones.append(tz_name)
            if friendly_name:
                self.timezone_names[tz_name] = friendly_name
    
    def remove_timezone(self, tz_name: str):
        """
        Remove a timezone from the clock.
        
        Args:
            tz_name: Timezone string to remove
        """
        if tz_name in self.timezones:
            self.timezones.remove(tz_name)


# Example usage
if __name__ == "__main__":
    # Create clock with default timezones
    clock = DigitalClock()
    
    # Optional: Add custom timezones
    clock.add_timezone('Asia/Bangkok', 'Bangkok (ICT)')
    clock.add_timezone('America/Mexico_City', 'Mexico City (CST)')
    
    # Option 1: Display once
    print("\n--- Single Display ---")
    clock.display_clock(include_date=True, include_seconds=True)
    
    # Option 2: Get times as dictionary
    print("\n--- Get Times as Dictionary ---")
    times = clock.get_all_times()
    for location, time_str in times.items():
        print(f"{location}: {time_str}")
    
    # Option 3: Run continuously (uncomment to use)
    # clock.run_continuous(include_date=False, include_seconds=True)
