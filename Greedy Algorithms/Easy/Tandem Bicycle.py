# O(NlogN) time and O(N) space
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()

    if fastest:
        blueShirtSpeeds.sort(reverse=True)
    else:
        blueShirtSpeeds.sort()

    totalSpeed = 0
    for idx in range(len(redShirtSpeeds)):
        totalSpeed += max(redShirtSpeeds[idx], blueShirtSpeeds[idx])

    return totalSpeed
