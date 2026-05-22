const requests = []

function thaw(now, period, shares) {
  requests.push({ until: now + period, shares })
}

function getThawed(now) {
  let thawed = 0
  for (const request of requests) {
    if (request.until > now) break
    thawed += request.shares
  }
  return thawed
}

const day = 24 * 60 * 60
let now = 0

thaw(now, 10 * day, 10)

const shortenedPeriod = 1 * day
thaw(now, shortenedPeriod, 10)

now += shortenedPeriod + 1
console.log('after shortened period, second request expired:', now > requests[1].until)
console.log('first request still unexpired:', now < requests[0].until)
console.log('thawed returned by creation-ordered traversal:', getThawed(now))

now += 10 * day
console.log('after original period, thawed returned:', getThawed(now))
