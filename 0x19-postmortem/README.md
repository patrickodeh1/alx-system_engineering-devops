# Postmortem Report: The Great TradeSphere Traffic Jam

## Issue Summary

**Duration:**  
Start Time: September 15, 2024, 09:00 UTC  
End Time: September 15, 2024, 11:30 UTC

**Impact:**  
TradeSphere's marketplace search feature decided to take an unscheduled nap. Users found themselves unable to perform location-based searches, which is kind of like being told you can’t find your way out of a paper bag. This affected approximately 60% of our users, who were left wandering aimlessly (virtually speaking).

**Root Cause:**  
Our load balancer had a bit of an identity crisis and decided to only share the workload with one server. As a result, that poor server was buried under a mountain of requests, leading to its dramatic collapse.

## Timeline

- **09:00 UTC:** The alert bell rang, signaling high response times and server errors. We had our first inkling that something was amiss.
- **09:05 UTC:** The on-call engineer, our tech detective, noticed increased error rates and response times.
- **09:15 UTC:** Investigation commenced. We first suspected the database might be playing hard to get, but it turned out to be well-behaved.
- **09:30 UTC:** We briefly entertained the idea that our application code might be the culprit but quickly realized it was not the case.
- **09:45 UTC:** The investigation turned to the load balancer, which had been misconfigured. Cue the dramatic music!
- **10:00 UTC:** The DevOps team took the stage and pinpointed the load balancer as the villain of the piece.
- **10:15 UTC:** Configuration was corrected. We gave the servers a much-needed break and rebalanced the load.
- **11:00 UTC:** The issue was resolved. Service was restored, and normalcy returned. Our users could once again navigate their virtual marketplace with ease.

## Root Cause and Resolution

**Root Cause:**  
Our load balancer decided to hog all the traffic for itself, leaving the other servers to twiddle their digital thumbs. This led to one server being overwhelmed and eventually failing.

**Resolution:**  
We reconfigured the load balancer to share the traffic evenly, like a good host at a party making sure everyone gets their fair share of the snacks. This fixed the issue, and our servers were happy once more.

## Corrective and Preventative Measures

**Improvements:**
- **Load Balancer Check-ups:** Think of it as a regular health check for our load balancer—no more sudden breakdowns.
- **Enhanced Monitoring:** More vigilant monitoring to catch any rogue traffic patterns early on. We’ll keep a watchful eye on our servers.
- **Documentation:** Better documentation so everyone knows what’s what with the load balancer. Knowledge is power!

**Tasks:**
1. **Patch Load Balancer Configuration:** Fix the configuration and run tests to ensure it behaves properly.
2. **Add Monitoring Alerts:** Set up alerts for unusual traffic patterns and server loads to prevent future mishaps.
3. **Conduct Regular Reviews:** Regularly review the load balancer settings and performance—think of it as a routine check-up.
4. **Update Documentation:** Keep documentation up-to-date so that our team can quickly understand and fix issues.

---

### Diagram: The Traffic Jam

![Traffic Jam Diagram](https://via.placeholder.com/500x300.png?text=Load+Balancer+Traffic+Jam)

---

For more details, visit the [GitHub repository](https://github.com/patrickodeh1/alx-system_engineering-devops/tree/master/0x19-postmortem) and check out the [README.md](https://github.com/patrickodeh1/alx-system_engineering-devops/blob/master/0x19-postmortem/README.md) file.

