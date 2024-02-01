
function getCurrentDateFormatted() {
    const daysOfWeek = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    const months = [
      'January', 'February', 'March', 'April', 'May', 'June',
      'July', 'August', 'September', 'October', 'November', 'December'
    ];
  
    const currentDate = new Date();
    const dayOfWeek = daysOfWeek[currentDate.getDay()];
    const dayOfMonth = currentDate.getDate();
    const month = months[currentDate.getMonth()];
    
    const formattedDate = `${dayOfWeek}, ${dayOfMonth} ${month}`;
  
    return formattedDate;
}
  
  // Example usage
  const formattedDate = getCurrentDateFormatted();
  document.getElementById('nav-date').innerText = formattedDate;
  