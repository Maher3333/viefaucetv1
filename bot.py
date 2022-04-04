# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzDQppbXBvcnQgc3lzDQppbXBvcnQgc2lnbmFsDQpmcm9tIGx4bWwgaW1wb3J0IGh0bWwNCmltcG9ydCBvcw0KaW1wb3J0IHRpbWUNCmltcG9ydCBqc29uDQpmcm9tIHJhbmRvbSBpbXBvcnQgKg0KaW1wb3J0IHBsYXRmb3JtDQppbXBvcnQgd2ViYnJvd3Nlcg0KZnJvbSBjb2xvcmFtYSBpbXBvcnQgRm9yZSwgQmFjaywgU3R5bGUsIGluaXQNCmZyb20gYnM0IGltcG9ydCBCZWF1dGlmdWxTb3VwDQpmcm9tIGNmZyBpbXBvcnQgY29vY2tpZSwgdXNlcl9hZ2VudCwgYmVhcg0KDQoNCmRlZiBkZWZfaGFuZGxlcihzaWcsIGZyYW1lKToNCiAgICBzeXMuZXhpdCgwKQ0KDQpzaWduYWwuc2lnbmFsKHNpZ25hbC5TSUdJTlQsIGRlZl9oYW5kbGVyKQ0KDQpkZWYgb3Blbl95b3V0dWJlKCk6DQogICAgaWYgcGxhdGZvcm0uc3lzdGVtKCkgPT0gIkxpbnV4IjoNCiAgICAgICAgb3Muc3lzdGVtKCJ0ZXJtdXgtb3BlbiBodHRwczovL3d3dy55b3V0dWJlLmNvbS9jaGFubmVsL1VDb1lXNGtSdzQyTEdibVRZUVBnMHpRQSIpDQogICAgZWxzZToNCiAgICAgICAgd2ViYnJvd3Nlci5vcGVuKCdodHRwczovL3d3dy55b3V0dWJlLmNvbS9jaGFubmVsL1VDb1lXNGtSdzQyTEdibVRZUVBnMHpRQScpDQogICAgdGltZS5zbGVlcCgxKQ0Kb3Blbl95b3V0dWJlKCkNCg0KDQpkZWYgbGltcGlhcigpOg0KICAgIHRpbWUuc2xlZXAoMikNCiAgICBpZiBwbGF0Zm9ybS5zeXN0ZW0oKSA9PSAiV2luZG93cyI6DQogICAgICAgIG9zLnN5c3RlbSgnY2xzJykNCiAgICBlbGlmIHBsYXRmb3JtLnN5c3RlbSgpID09ICJMaW51eCI6DQogICAgICAgIG9zLnN5c3RlbSgnY2xlYXInKQ0KDQpsaW1waWFyKCkNCg0KDQpkZWYgY29udGFkb3Ioc2Vjb25kKToNCgl3aGlsZSBzZWNvbmQ6DQoJCW1pbnMsIHNlY3MgPSBkaXZtb2Qoc2Vjb25kLCA2MCkNCgkJdGltZXIgPSBscm9qbysiIOKWtiAiK2xjeWFuKyJFc3BlcmUgIitsYW1hcmlsbG8gKyBcDQoJCSAgICAiKHs6MDJkfTp7OjAyZH0pIi5mb3JtYXQobWlucywgc2VjcykrcmVzdGNvbG9yDQoJCXByaW50KHRpbWVyLCBlbmQ9IlxyIikNCgkJdGltZS5zbGVlcCgxKQ0KCQlzZWNvbmQgLT0gMQ0KDQoNCmRlZiBsZW50byh0ZXh0byk6DQogICAgdHJ5Og0KICAgICAgICBmb3IgbGV0cmEgaW4gdGV4dG86DQogICAgICAgICAgICBwcmludChsZXRyYSwgZW5kPScnLCBmbHVzaD1UcnVlKQ0KICAgICAgICAgICAgdGltZS5zbGVlcCgwLjA4KQ0KICAgIGZpbmFsbHk6DQogICAgICAgIHBhc3MNCg0KZGVmIHViaWNhY2lvbigpOg0KICAgIHViaWNhY2lvbiA9ICJodHRwOi8vaXAtYXBpLmNvbS9qc29uIg0KICAgIHJlcyA9IHNlc3Npb24uZ2V0KHViaWNhY2lvbikNCiAgICBwYSA9IChyZXMudGV4dCkNCiAgICBwYSA9IGpzb24ubG9hZHMocGEpDQogICAgcGFpcyA9IHBhWydjb3VudHJ5J10NCiAgICBwcmludChmIntmbGJsYW5jb317bG5lZ3JvfSBFc3RhcyBDb25lY3RhZG8gRGVzZGU6IHtyZXN0Y29sb3J9e3Jlc2V0Zm9uZG99IiArZmxyb2pvK2xhbWFyaWxsbytwYWlzK3Jlc2V0Zm9uZG8rcmVzdGNvbG9yKQ0KICAgIA0KDQoNCiMgdmFyaWFibGVzIGRlIGNvbG9yDQphenVsID0gRm9yZS5CTFVFDQpuZWdybyA9IEZvcmUuQkxBQ0sNCmN5YW4gPSBGb3JlLkNZQU4NCnZlcmRlID0gRm9yZS5HUkVFTg0KbGF6dWwgPSBGb3JlLkxJR0hUQkxVRV9FWA0KbG5lZ3JvID0gRm9yZS5MSUdIVEJMQUNLX0VYDQpsY3lhbiA9IEZvcmUuTElHSFRDWUFOX0VYDQpsbWFnZW50YSA9IEZvcmUuTElHSFRNQUdFTlRBX0VYDQpsdmVyZGUgPSBGb3JlLkxJR0hUR1JFRU5fRVgNCmxhbWFyaWxsbyA9IEZvcmUuTElHSFRZRUxMT1dfRVgNCmxyb2pvID0gRm9yZS5MSUdIVFJFRF9FWA0KbGJsYW5jbyA9IEZvcmUuTElHSFRXSElURV9FWA0KZmxhenVsID0gQmFjay5MSUdIVEJMVUVfRVgNCmZsY3lhbiA9IEJhY2suTElHSFRDWUFOX0VYDQpmbHJvam8gPSBCYWNrLkxJR0hUUkVEX0VYDQpmbHZlcmRlID0gQmFjay5MSUdIVEdSRUVOX0VYDQpmbGFtYXJpbGxvID0gQmFjay5MSUdIVFlFTExPV19FWA0KZmxibGFuY28gPSBCYWNrLkxJR0hUV0hJVEVfRVgNCnJlc3Rjb2xvciA9IEZvcmUuUkVTRVQNCnJlc2V0Zm9uZG8gPSBCYWNrLlJFU0VUDQpicmlsbG8gPSBTdHlsZS5CUklHSFQNCnAgPSAoZiJ7bHZlcmRlfSAiKQ0KaG9yYSA9IHRpbWUuc3RyZnRpbWUoIiVIOiVNOiVTIikNCg0KIyBjb29raWUgPSBjb29raWUNCg0KDQppbml0KCkNCg0KZGVmIGVzdGFkbygpOg0KI'
love = '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'
god = 'RhZG8oKQ0KIyBsZW50byhCYW5uZXIpDQoNCmxpbmVhID0gIi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4iDQpsZW50byhsaW5lYSkNCg0KaGVhZGVycyA9IHsNCiAgICAiSG9zdCI6ICJ2aWVmYXVjZXQuY29tIiwNCiAgICAiYWNlcHQiOiAiYXBwbGljYXRpb24vanNvbiwgdGV4dC9wbGFpbiwgKi8qIiwNCiAgICAiYXV0aG9yaXphdGlvbiI6IGJlYXIsDQogICAgInVzZXItYWdlbnQiOiB1c2VyX2FnZW50LA0KICAgICJhY2NlcHQtbGFuZ3VhZ2UiOiAiaWQtSUQsZW4tVVM7cT0wLjkiLA0KICAgICJjb29raWUiOiBjb29ja2llLA0KICAgICJ4LXJlcXVlc3RlZC13aXRoIjogIm1hcmsudmlhLmdwIiwNCn0NCiMgaW5pY2lhbW9zIHNlY2Npb24NCnViaWNhY2lvbigpDQp0cnk6DQogICAgaW5kZXggPSAiaHR0cHM6Ly92aWVmYXVjZXQuY29tL2FwaS91c2VyL21lIg0KICAgIHJlc3B1ZXN0YSA9IHNlc3Npb24uZ2V0KGluZGV4LCBoZWFkZXJzPWhlYWRlcnMpDQogICAgcGFyc2VyID0gaHRtbC5mcm9tc3RyaW5nKHJlc3B1ZXN0YS50ZXh0KQ0KICAgIGNvbnRlbmlkbyA9IHJlc3B1ZXN0YS50ZXh0DQogICAgY29udGVudCA9IGpzb24ubG9hZHMoY29udGVuaWRvKQ0KICAgIHVzdWFyaW8gPSBjb250ZW50WyJ1c2VyIl1bInVzZXJuYW1lIl0NCiAgICByZWNsYW1vcyA9IGNvbnRlbnRbInVzZXIiXVsiZmF1Y2V0Q2xhaW0iXQ0KICAgIHJlY2xhbW9zID0gc3RyKHJlY2xhbW9zKQ0KICAgIGJhbGFuY2UgPSBjb250ZW50WyJ1c2VyIl1bImJhbGFuY2UiXQ0KICAgIGJhbGFuY2UgPSBzdHIoYmFsYW5jZSkNCiAgICBwcmludCgi4pyU77iPIitmIntsdmVyZGV9IFVzdWFyaW86ICIrbGFtYXJpbGxvK3VzdWFyaW8rbHJvam8rIiB8ICIrbGJsYW5jbysi4pyU77iPIitmIntsdmVyZGV9IEJhbGFuY2U6ICIrbGFtYXJpbGxvK2JhbGFuY2UrbHJvam8rIiB8ICIrbGJsYW5jbysi4pyU77iPIitmIntsdmVyZGV9IENsYWltczogIitsYW1hcmlsbG8rcmVjbGFtb3MrcmVzdGNvbG9yKQ0KICAgIHRpbWUuc2xlZXAoMikNCmV4Y2VwdCBFeGNlcHRpb24gYXMgZToNCiAgICBwcmludChmIntmbHJvam99e2x2ZXJkZX0gRXJyb3IgZGUgRGF0b3MgdmVyaWZpcXVlIGNvb2tpZSB5IGJlYXJ7cmVzdGNvbG9yfXtyZXNldGZvbmRvfSIpDQogICAgc3lzLmV4aXQoMykNCmxlbnRvKGxpbmVhKQ0KcHJpbnQoZiJ7bGF6dWx9IEluaWNpYW5kbyBjbGFpbSBGYXVjZXR7cmVzdGNvbG9yfSIpDQp0aW1lLnNsZWVwKDIpDQojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0NCndoaWxlIFRydWU6DQogICAgdHJ5Og0KICAgICAgICBob3JhID0gdGltZS5zdHJmdGltZSgiJUg6JU06JVMiKQ0KICAgICAgICBmYXVjZSA9ICJodHRwczovL3ZpZWZhdWNldC5jb20vYXBpL2ZhdWNldCINCiAgICAgICAgcmVzcG9uY2UgPSBzZXNzaW9uLmdldChmYXVjZSwgaGVhZGVycz1oZWFkZXJzKQ0KICAgICAgICBsaW1pdGUgPSAocmVzcG9uY2UudGV4dCkNCiAgICAgICAgIyBwcmludChsaW1pdGUpDQogICAgICAgICMgY2FwdHVyYW5kbyBjYXB0Y2hhIHkgYW50aWJvdGxpbmsNCiAgICAgICAgYW50aSA9ICJodHRwczovL3ZpZWZhdWNldC5jb20vYXBpL2FudGlib3QiDQogICAgICAgIHJlc3B1ZXN0YSA9IHNlc3Npb24uZ2V0KGFudGksIGhlYWRlcnM9aGVhZGVycykNCiAgICAgICAgYW5zID0gKHJlc3B1ZXN0YS50ZXh0KQ0KICAgICAgICBzb2x1Y2lvbiA9IGpzb24ubG9hZHMoYW5zKQ0KICAgICAgICBzb2x2ZV9hbnRpID0gc29sdWNpb25bImFudGlib3QiXVsiYW5zd2VyIl0NCiAgICAgICAgYW50ID0gc29sdmVfYW50aQ0KICAgICAgICBwcmludChmIntsdmVyZGV9IEFudGlib3QtbGluayBDYXB0dXJhZG97cmVzdGNvbG9yfSAgICAgICAgICAgIiwgZW5kPSdccicpDQogICAgICAgIHRpbWUuc2xlZXAoMykNCiAgICAgICAgIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tDQogICAgICAgIGNhcHRjaGEgPSAiaHR0cHM6Ly92aWVmYXVjZXQuY29tL2FwaS9jYXB0Y2hhIg0KICAgICAgICByZXNwdWVzdGEgPSBzZXNzaW9uLmdldChjYXB0Y2hhLCBoZWFkZXJzPWhlYWRlcnMpDQogICAgICAgIGFuczEgPSAocmVzcHVlc3RhLnRleHQpDQogICAgICAgIHNvbHVjaW9uMSA9IGpzb24ubG9hZHMoYW5zMSkNCiAgICAgICAgc29sdmVfY2FwdGN'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
