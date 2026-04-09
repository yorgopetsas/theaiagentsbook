-- Weekly lead reporting pack (Cloudflare D1)
-- Run these queries in the D1 console.

-- 1) Total leads (last 7 days)
SELECT COUNT(*) AS total_leads_7d
FROM leads
WHERE datetime(created_at) >= datetime('now', '-7 days');

-- 2) Daily leads (last 7 days)
SELECT date(created_at) AS day, COUNT(*) AS leads
FROM leads
WHERE datetime(created_at) >= datetime('now', '-7 days')
GROUP BY day
ORDER BY day DESC;

-- 3) Leads by audience (last 7 days)
SELECT COALESCE(audience, 'unknown') AS audience, COUNT(*) AS leads
FROM leads
WHERE datetime(created_at) >= datetime('now', '-7 days')
GROUP BY audience
ORDER BY leads DESC;

-- 4) Leads by landing page (last 7 days)
SELECT COALESCE(landing, 'unknown') AS landing, COUNT(*) AS leads
FROM leads
WHERE datetime(created_at) >= datetime('now', '-7 days')
GROUP BY landing
ORDER BY leads DESC;

-- 5) Leads by UTM content (button/page variant) (last 7 days)
SELECT COALESCE(utm_content, 'unknown') AS utm_content, COUNT(*) AS leads
FROM leads
WHERE datetime(created_at) >= datetime('now', '-7 days')
GROUP BY utm_content
ORDER BY leads DESC;

-- 6) Leads by source/medium/campaign (last 30 days)
SELECT
  COALESCE(utm_source, 'unknown') AS utm_source,
  COALESCE(utm_medium, 'unknown') AS utm_medium,
  COALESCE(utm_campaign, 'unknown') AS utm_campaign,
  COUNT(*) AS leads
FROM leads
WHERE datetime(created_at) >= datetime('now', '-30 days')
GROUP BY utm_source, utm_medium, utm_campaign
ORDER BY leads DESC;

-- 7) Duplicate email check (all time)
SELECT email, COUNT(*) AS hits
FROM leads
GROUP BY email
HAVING COUNT(*) > 1
ORDER BY hits DESC
LIMIT 100;
