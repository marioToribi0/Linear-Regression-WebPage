/**
 * Minified by jsDelivr using Terser v5.7.1.
 * Original file: /npm/chartjs-plugin-trendline@1.0.0/src/chartjs-plugin-trendline.js
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
/*!
 * chartjs-plugin-trendline.js
 * Version: 1.0.0
 *
 * Copyright 2021 Marcus Alsterfjord
 * Released under the MIT license
 * https://github.com/Makanz/chartjs-plugin-trendline/blob/master/README.md
 *
 * Mod by: vesal: accept also xy-data so works with scatter
 */
var pluginTrendlineLinear = { id: "chartjs-plugin-trendline", afterDraw: function (t) { var i, e; for (var a in t.scales) if ("x" == a[0] ? e = t.scales[a] : i = t.scales[a], e && i) break; var s = t.ctx; t.data.datasets.forEach((function (i, a) { if (i.trendlineLinear && t.isDatasetVisible(a) && 0 != i.data.length) { var r = t.getDatasetMeta(a); addFitter(r, s, i, e, t.scales[r.yAxisID]) } })), s.setLineDash([]) } }; function addFitter(t, i, e, a, s) { var r = e.trendlineLinear.style || e.borderColor, n = e.trendlineLinear.width || e.borderWidth, o = e.trendlineLinear.lineStyle || "solid"; r = void 0 !== r ? r : "rgba(169,169,169, .6)", n = void 0 !== n ? n : 3; var l = new LineFitter, d = e.data.length - 1, h = t.data[0].x, u = t.data[d].x, m = !1; e.data && "object" == typeof e.data[0] && (m = !0), e.data.forEach((function (t, i) { if (null != t) if ("time" === a.options.type) { var e = null != t.x ? t.x : t.t; l.add(new Date(e).getTime(), t.y) } else m ? l.add(t.x, t.y) : l.add(i, t) })); var x = a.getPixelForValue(l.minx), c = a.getPixelForValue(l.maxx), f = s.getPixelForValue(l.f(l.minx)), g = s.getPixelForValue(l.f(l.maxx)); m || (x = h, c = u); var p = t.controller.chart.chartArea.bottom, v = t.controller.chart.width; if (f > p) { var w = f - p, X = f - g; f = p, x += v * (w / X) } else if (g > p) { w = g - p, X = g - f; g = p, c = v - (c - (v - v * (w / X))) } i.lineWidth = n, "dotted" === o && i.setLineDash([2, 3]), i.beginPath(), i.moveTo(x, f), i.lineTo(c, g), i.strokeStyle = r, i.stroke() } function LineFitter() { this.count = 0, this.sumX = 0, this.sumX2 = 0, this.sumXY = 0, this.sumY = 0, this.minx = 1e100, this.maxx = -1e100 } LineFitter.prototype = { add: function (t, i) { t = parseFloat(t), i = parseFloat(i), this.count++, this.sumX += t, this.sumX2 += t * t, this.sumXY += t * i, this.sumY += i, t < this.minx && (this.minx = t), t > this.maxx && (this.maxx = t) }, f: function (t) { t = parseFloat(t); var i = this.count * this.sumX2 - this.sumX * this.sumX; return (this.sumX2 * this.sumY - this.sumX * this.sumXY) / i + t * ((this.count * this.sumXY - this.sumX * this.sumY) / i) } }, void 0 !== typeof window && window.Chart && (window.Chart.hasOwnProperty("register") ? window.Chart.register(pluginTrendlineLinear) : window.Chart.plugins.register(pluginTrendlineLinear)); try { module.exports = exports = pluginTrendlineLinear } catch (t) { }
//# sourceMappingURL=/sm/00e48d45f69aa04c5677bccb5085ccd9154cb3b9145fa0fb4f42e008cc26732a.map