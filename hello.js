function calculateMoney(ticketNum) {
    if(ticketNum <= 0){
        return 'invalid Number'
    }
    let ticketPrice = 120;
    let PerDayDarowan = 500;
    let stupLunce = 8 * 50;
    let totalDrawanAndLunce = PerDayDarowan + stupLunce;
    let totalTicketSellPrice = ticketPrice * ticketNum;
    let totalTaka = totalTicketSellPrice - totalDrawanAndLunce;
    return totalTaka
}
const ticket = 10;
console.log(calculateMoney(ticket));