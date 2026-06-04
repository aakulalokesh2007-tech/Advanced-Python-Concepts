from tkinter import*
import random
from PIL import Image,ImageTk
import io
import base64
encode_image="""/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxAPDw8OEA8QDw8PEBAPDQ0PDw8PDw0NFRUWFhURExYYHSggGBoxGxUVJTEhJSwrLi4uFyAzODMsOSgtLisBCgoKDg0OGhAQGislHR0tLS0tLS4tLTAuKystLS0tLS0tKy8tKzcrKy0vKy0tLSsrLSstKysrLSsrLS0tKystK//AABEIAKUBMgMBEQACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAAAAQIEBQYDBwj/xABCEAABAwMCAwYDBAcECwAAAAABAAIDBAUREiEGEzEHIkFRYXEUMpEjgaGxMzRScoKSwRVDU2IkQmODk6KjsrPC4f/EABsBAQABBQEAAAAAAAAAAAAAAAABAgMEBQYH/8QANBEAAgEDAgIGCQUBAQEAAAAAAAECAwQRBTESIQZBUWFxkRMiMoGhscHR8BRCUuHxIxWi/9oADAMBAAIRAxEAPwCGutNCCAEAIAQAgBACAEAIAQAgBACAEAIQCAVACEZBACARCQQAgBCQQAgBACAEAIAQAgBACAEAIAQAgBACAEAIAQAgBACAEAIAQAgBACECoQGEGRcKSMhhCMi4QjIYQZDCE5EwgyJhQTkEJEQkEJBACAEAIAQAgBACAEAIAQAgBACAEAIAQAgBAIgOXxLM41DKt+lhnGSrglvg6q4UioAQAgBCBUIFwpKci4QjI7CFORcIRkMIRkMIMhhCciYQnIhCEpjSEKsiKCrIISIgBCREBzdM0eKtyqwjuypQk9kK2Vp6FTGpGWzIcWtzoqyAQAgBACAEAIAQAgBACAEAIDhVz6APNxDW56ZKx7q4jQpupLqLlGk6klFEm42GrjhEgIl1gamN6sB8lx1HpYqk5QmsLqNzLSuFJosL/bIYKCLEYEjiwF3+tnxWj0m4rV9RWZPGTOuoRhbvkVjeg9l6ocoKpAIAQgVCBwCkpbHAIUNjgEKWxQFJQ2O0oRxC6UI4g0oOITSg4hCEKkxpCFSY0hQVpjSEKkxCoKkxEKhEBE1OllbAzqep8lpdW1JWtNvrM+ztvSyNULPS07AZ3DUeuV51V1O7uZtwbOhjbUqa5nKtsMMsZlp3dBnZXrPWbm3qJVGUVrOnUjyM/A47td8zdivTbK5VxSU0czXpOnLB2WYWQQAgBACAEAIAQAgBACAEBHrqRszCx33EdQfNWqtKNWLjIrpzcHlFjwVeKiKX4Kb7RmMxyHqB5Fea9ItHja/9Y9Z02n3TreqzScQUQq4+Xq0uadTceB9Vz+n3s7OsqsUbGvbRqwcDGuD4n8mUaXjofB48wvWNL1alfU8xfPsORu7OdCXPY6rbmGCECoQxwCkpbHAIUNjwFJbbHAIUNjgFJQ5Dg1CniF0oRxBhBxBpQcQ0tQqUhpCgrTGEIVpjSFBcTGEIVpiKCpDXIypHHgx4+NeXdR0XnnSqUjpdLimiTxw4vlIcSG42VPRmnSlF8W41Jzi1gldncrxFI12S3fGVqNejCNf1TMsU5Q5kCrx8TJjpldt0ZcnbLJo9USVQcumNWCAEAIAQAgBACAEAIAQAgBANtNwhhrC6Z4YBHtnxXE9LoVKsYwgsm90Zxg3KRDuN3nfVvqqOTXG3DdB+V4WHp+genssTXMyLjUPR1+T5A2SoqZRUVGG4GGRjo1dHo2jRsVnrNZfXzr8ict+a0VCkUBSUseAhQ2PAUltseAhbbKmr4mpYpDDrdJKDpMcTHSO1fs7bE+ixal7RpvDfNdhkU7KvUWUuT7QmvU7Y3z/2VcBDG0vfNJTuijazzLjkLGeq0+qL+BfWk1euS+I2qudbSQ01ZXUjIqKsbqp5IpA+RupmtgeM9S3B8PwwrdPVcy9dcu4uVdJxH1Jc+/8APuXVl4Tu1wibVyVMNqppGh8LDGJ53Rn5XyasBuRjG469FjVdTqyfq8kZNLS6MV63NkKppKqguLbdNVx1zX03xImbFynxguLQCBtg48z1H35Wn3lWrPgnzRiajZ0qVPjhyeSywtwaXIhCglMaQhWmMIUFxMYQhcTGEKC4mMIQuJjSoKkUj5XUlSJwO6T3lzGu6c68Hg3Gn3PA+ZsfjKSsYC5wBxvlefxhdWkmo5OibpVlzFluFPTRlkOCT0wrlCxubyqnJFNSvSoQ5FBACS57urjlep6daK2oqJyV1W9LNs7rYGMCAEAIAQAgBACAEAIAQAgBARaq3xSkF7A4joSrU6MJvMkVxqSjsztBA2MaWNDR5BVxiorCKXJvc6KogEIHBCljgFJSx4CFpse0KS22OewlpAOCQQD5EjqjWVgt8WHkxfA/HNXYhLTmmZpmnY6R8zJNTA3uv04I1bY/+5XJVKcovElg62FSM1mLyb/t84mrKVsNLBK1tNWwzx1DeXG9z9JAc3U4HA0vHTB2VqOGXGZa+WyJ/DVrrzNVz8qaNssMs73xRwB0sb2RMOze8xoB8sBTnngYNP2708tVHQOjEzqFhlM/w7Obokc1vJkLARkY1AHwyemRlScXLEuRTU4lHMebMPwhTPt7421VLLTmu1CkqZho5jWnHLLDuwk4O/XLfAgra6bXpxm4Pd9f0NTqtCrOCmnyjuvr3m4wt8c7kQhCcjSEKkxhCguJjCFBcTOZCF1M5kKC4mNKFxHKWIOGHDIVMoqXJlabWxBNpYDlpI9lhT0+jN5aMiNzNdZIhpGt9T6q9StadP2UUTrSnuyQsgtCoAQAgBACAEAIAQAgBACAEAIAQAgBAKhAoQoY9qkoZ0aFJabOjQpLMmdAELbZje0+DMFPJ4tlczPo9uf/AEWr1WPqRl2P5/4bTR5/9JR7Vny/07dqfFVFcqO3cmYvqYhmeMxyt5XMjZraXOABIcwDYlc/CLTZ0LeR1tq6mfh59oZbbhLMZA6GaOle6nEfObLkv6g/P4Y3G6nHrZGeWCw7LeIL9LByKSliraenLYhJPI2J1OCO7Hr1guaBnbBI2GQMBRKEW8kpspbtxHcLjVRx1LGuqYKow0logBY345pwZJcknAO2S7wIGBqKyaChSXpOtbLv7X3fMxa/HU/5Lkmub7uxd/yNtJwNWNLBV8RU1HUyguZSiGEt9mlz2lw9dJ+9XXqFdvPEWo6bbJY4fmZGz8aRGINne6WcPcxohhdqmYPlfjYAnyWxpanCNLNZ81+eBq6+lVHVxRXq97/GWkd3q5f1e01r/Iyt+Hb9SCFiVuktlT/cvNfTJep6DXlu/g/rg7x0F8l+WjpaYec84kOP92f6LWVumNvH2Ofuf1wZtPo9/Jv4f2SGcHXaT9JcKaDzEEBl/F4BWsq9NJP2Iv4L7mbT0Kkt/r/RWXyz1NrlopJK59XHUTmnma6JsbWucO4QMn1+iztE6Q1b244JrC5ded+XYu4tX2m06VFuK5li4Ltjn0xhQuIaVBUhChUCAEAIAQAgBACAEAIAQAgBACAEAIAQAgAIBQhSOCkoY9qFtjnyNYNTnNaPFziGj6lG0lllvDbwisqeKaKLrUNcfKMOk/Fox+Kxp3tCP7vLmXI2Nee0fPkOhvFTN+q2ysl8nyN5EZ9dRyFq7jpJZ0v3LzXyWTMp6FXn7Tx7v8H1nDF3r4zFNDRU0TsEtkkfJKwjoQWZGVobvpdbzi4KOV3L6tr5G0tdCdKSnxPP53EUcGVFgaLzDURVE9H3uQ+nfyix4MTiSHgnAfnw6LXWmuRuK6pcGE+vP9GyqWrhHiya++8c10nDUF1glbT1ZlAqDHGxzeWJZIiGh4cBuIz5rd8s4MXqI3ZfFVQ8POlomh9ZU1oqWNc5kbHRsmiZIwk9AWRSDb9rZRKSTwyUmd+J7bFRcR2286QyGpkdT1Or5WVroXxxPPlkEexjcT1UKWU8BrBme0fgC5113mqIYxJDUGLTM6VjWwAMaxzXgnUACD0ByMYydlMakccw4suOya3yUbLhRTBomp6vD9JDgQ6NuCD5ENyPdcn0iX/aEu2P1/sz7P2Wu83q54zQQHKoqY4xmSRkY8S97WD8VVGEpcopvwIbS3PPO1C+Uc9JCyGqhmnjq4ZY44ZGyE41NPy5/aXSaBb3FG6U5QaWOtY60/oYF7OE6TWTo9etHExOZUF1DCoK0IhIISCAEAIAQAgBACAEAIAQAgBACAEAIAQAEIFCEMcFJQyBxFXPp6WWZmNbQ0NJ6NLnBur8VYuqrp0nKO5Vb01UqqL2JfAXB1DW0UFdUtlqZpNevnTvLWuY9zcANI22Bwc9V5dq+rXcLiVNSwljn181nd5+B19ta0uBPBv7fZ6Wn/QU0MPrHExpPuQMlc9VuKtX25N+LM2MIx2ROVkrBAZrjC90IpKunmq4GukgljEYka+TU5pA7jcnr6LY2FrcOtCcIPCaecct+0sVakOFps8qtvFrXWOWyfDzSzyykwOjwWtbzI5RsMuJ1NfsB0K7yWIvjk8JGqWXyRotN7ntVLbae3SUbYdBdUfEthkkA1lwLHFrmgufkj0WvnqtlCTzUy+7L+SLqoVWtiuu9JxC22i2y0vMpWb62COonLQ/WBqa5zgAemANtuimnqllOXKaz35XzEqFVLYzTOOLtFF8MK6oa1oLMF32rB006yNYx067LYpRfNFnLNn2GVRMtwa5xc57YZSXEklwc8Fx9e+N1zfSSPq05eK+X2M2yfNo9bC5Q2B4BVPqHzVTJ7xLCIamaERyzzyPIY4jIbq6eH3L0uwsbWrRjUahHKX7VnbJzl1dVqc+CMZS9/Ir2W+2579dNM4nflU72En+LK2apWkVzqP3LHzMZ1buW1NLxefkabhi128uMkAkdLCQHc/IkjJGx07DzwVsLKnay9elza7TAu6tzH1KnJPsNK5bIw0cyoLqGlQVoahUCEggBACAEAIAQAgBACAEAIAQAgBACAEABCBQhDHBSUMj3al51PNEOr43Bv7+Mt/EBW60OOnKPaiKU+CopdjKLs/7QYbbSPppoppTzXSQ8vRpDXNaC0kkY3Geh6lebanpE7qsqkGlyw8nX0LhU44ZY1nbDLsYqFrGF2A+V75NTQe9gANGcepwrMOjcUszm/csfcqd9l4SPXAQQCOh3HsuU2NgeY9ucT+RSSte4M5kkUjA4hry5ocwkZwcaH/VdH0clH0k4tc8Jr6/NGHep4TPM+FuH5bjUsposNz3pZCMtiiGNTyPHqAB4khdHeXcLWk6k/cu19hhU6bqSwj6D4b4apbdGI6eMBxAEk7sGaU+bnf0G3ouDu72tdS4qj8F1I21OlGCwi4wsQuAgMlx3wTDconPa1sdY0fZT4xzCP7uXzHr1H1B2mm6nO0mk+cHuuzvX5zMevQVRZ6zzzsbLobrLC8FrzTzROYdiJGPYSCPMaSt/r2J2inHbKfuaf3MS05VGme4LjDZlW7h6h5jpnUlMZXuL3Svhjc8vPV2XDqsn9ZccKgpywurLKPRRznBOj5cezQxg8mNA/JWJSct3kuKD6keb3hgjvtTjpU0cU5/eaWx/k0r0nobVcqHD2Z+efqcvr1PDT7/AKf0SnLtTn0cyoLqGlQVoahUIShImoKMjAuVIBAKgBACAEAIAQAgBAIgItVXsj6nfyVmpWjBcyuFNy2IsdZJJ8jT9Fqq+s0qfWZkLKUjsY6kb6CsSPSCk3uXXp0hrK8g4e0hbO31KlV2Zi1LWUSdFIHDIK2MZJ7GK1g6BVFLHBSUM6NUltnKOghDi8QxB5OXPEbA4nzJxlUKlBPKis+BRKpNrHE8eJQdo8GqkjeB+jmA9muaR+YasHVI5pJ9jMvS5YrNdqPUeEa3n2+imJBLqeIOP+drdLvxBXjd9T9Hc1I9jf3O5ovigmUvavTCa0zkd50Lophjww4Ncf5XuWXolTgvIr+WV8Puii7g/RNlT2IW4Mo56nHfnm5YP+yjaMD07z3fQLL6RVnKvGn1RWfe/wDEWrOOIt9po+OOJH0MUbII+bV1TzHSxnpkY1SO9BkfXyysPSNNlfVuDqW/0RVd3MaFPiZ51VcM3Gsy+suLi525jBe+NvoGgtaPYDC9Jtuj9OlFcKjHwWX5nKVdeTfJN+/HwKuoguNkcyeGpc6HUAQ0u5RP7MsZOMHff8QcLF1LRoOP/SKafX1ozLHVFVeI5TXUe2WC7srKSCrbhomjDi3OdD+j258cOBH3LzO6oOhWlSf7X/nwOnpy44qSPO7hA2m4rppGnDapokwOmuSOSI/Vzc+5W/pTdbR5p/t5eTT+RhyjwXK7z0gyOPiVzBt+FGP4y41dbp46dlGah0sIma/mub1c9pbpDDnGnz8Vu9M0dXtNz48YeMYz1J9vf2GBdXjoyxgzzuO7xKcQ26ONp6F8Mzj/ADPcGn6LfUuikHupv4L5fU1tTWYr90QtkNbLUGvuD2iURciKMCJobFqLt9G3UnzO66vSNKjYxeFhdmc+/wCBotQv1c4jHn3l0TncbjzW7NakMKF1DCoK0cp5Q0KmUsFyKyVFRct8BYFa7UDJp0cjGzvO+6wf/TjkyP0rOjatw6q/DUIvrLcrZol09blZ9OupGPOm0TWnKyEWRykAgBACAEAIAQFddq4RMPmsevVVOJdpU+JkXhmzSVsmt+dGVw+r6s45SZvrW1R6lb7LDC0DSNvFcXVuqlR5bNrGmoksxQnbDVa4p7lWEVd14cimacAA+izLbUKlKW5aqUYyRgaylfSS6TnTnZeg6Nq3pkk2aG8tOHmifG/IBXVp5Rp2sHQKooY9qFtnRpUlmSKziun5lDUt8mcwfwEP/JqxryHFQku7PlzLtnLhrxffjz5Fn2TVfMtbGeNPPNF9zsSg/wDUP0XkWv0+G74v5JP6fQ9A0+WaeOw092pOfTVMH+NBNGP3nMIH44Wrtqnoq0J9jT+JlV48VNoy3Y1XA218YxmKpeCP8rmtcD9dX0W36QwcblS7UvhkwbFKUGuw69o0cjXUNyawvZRSSCpYwZc2CUNHMA9MH6hZfRa+hb3LjP8AdjHx5ePPl4GNrNo6tBxj+fmCNDxBRvaHCqgAIzh0rGO+9riCF6mrqi1njXmcBKzuIvDg/IpOJ7pHWxOoKTNVUTGMNbC0uawB7XFxd0A26+Gd8LW6pqFvChJOS8fz6Gz0uwrqspuOEs/LB6Bw3a/gqKmpCQXQx4kIOWmVzi9+k+I1OOF5BfXH6i4nVWzfLwXJfA9Bt6fo6aizzztCr2sv1A4OH+jNo+Zv8p5zpcH+F4+q6PSaLenVFj2uLHlj5o1t1JfqE+zB6vIMEjyJXIm4WxmeKuGpqyelqIKplK+nZMxz3RmRxD8Yw3odi7r6LeaPrH/nqTSbb2+prr6xV1ylsQW8CPf+sXWsk8xCG07fpkrYVul11P2Vj3v6YMWnodCPUvL75O8XZ1bcgyMqJz4umqXkn+QNWuqa/ezecpe775MyGnUooznD8PIfXUe+mlrJWRA74hJOn8ifvXpmhXDrWkZPufmvvk5LU6ahW5FsVuTBQ0qCtFPeptLSsW4lhGRSWWUNp+0lAPmuT1Gs0mbm3gj0+2WBrmA48FyFa9kpbmzjSWDnceGwGkgK5Q1KWdymdBGMqoDFJj1XY6ZdueDU3VJItKR+WrrKbyjTyXM6ulA8VVxIjArZAVKaIwOUgVACAEAhKgGPu0hmqGxjplc9qtxwxZtbOnk9e4UomwQNGN8BeYXtZ1KjOkpU8RI/Fd95DdLT3isrTbB3EyzcVvRo86q+JKqJweSdJK6ypoUIQ2NbC9cpHpPB96+KiBPXG64y/tvQzwbWlPiRH44oQ6LXjcLJ0i4dOqi3cwUomRtUmW48l63aT4qaZyVeOJE8LKMdjwpLbHgqS20LIwPa5h6PaWn2IwVDWU12lv2XldRSdi85a6vpXHdvKlDfItLmPP8AzMXlXSWjjgn2ZT/PM73TZpt956ew4IPkQVyht2so8d4avLbTeK2ml7lLLPJC8/4Qa93Kl9sH6OJ8F2l5au+soTj7aSa7+XNfnWjSUavoazT2PYQehBBBGQQQWuafEHxC4xpp4Zuk1JFTNwzb3uL3UNKXHckQtbk+ZAwFmR1G6isKpLzLLtaT6ifR0kUDSyGGKBp6thjZGD76RusepWqVXmpJvxeS5ClCHsoiX+9wUEBqJztuIoge/PJ4MYPzPgr1nZ1LqooQXi+wor140o5Z4zxdb5uWyvqf1mrme+Vu4EbXNBjjx4YDT+A8F6d/56tLWml4fnfu2clSvv1FxNLZfj+h7pRy86KKZoJE0UcoIGQQ9gd/VeVVocFSUH1NryOvpTTgmE8rIxmR8cYHUySMYAPvKiNOc/ZTfgip1ILdlVU8V26IEur6bA/w5OcfpHnKzIaZdz2pv3rHzwWZXdJdZUVfaXa4/lkmn9IoCP8AyFqy6eg3ct0l4v7ZLUtQprYz1nrRV1dfXMjfHBUvi5QkxqJY0hx29fz9F6N0dtalvbcE+rln3v7nK6rVjUqLH5sW5XQGtQhUFRQ3/wCUrCudjKo7lRw4fth7rj9S2Zu7c9tsf6Mey4e49o20NiXXDuFWqftEvY8s4lIEhXb6NLGDUXaIENdtgLsf1KjE0/om2ITI7cArW1tUjF7mVC1yh0c7mHdX7bUFPrLVW2aLSnqA4LcQqKSMKUcEjKulAqAEBznPdPsqZbEx3Mja+9XDP7S47Wm+Fm9slse0Uu0bceS83qc5nSR9kwHEshdU4d0yu96NU44yc/qcmZ/ieRulrB12XVX00oGqtotyN52bUpjhBPivL9XqqVTkdNbQaiXXGEoFOfZY2mxbrIrr8oswVoGxK9fsFikjkLl5mWIWcYzHBSUMe0oW2jo0qS20ZPhepbRcQSte5scc4mY573BrWiRnNbudsag0LhOk1q506iistNNe/wDps6vSa3qwb7MeX+HoNdxhbYRl9dC70hJqCf8AhghcTS0q7qbU2vHl88G+leUo9Z5zV0EN5rK+qi5kcTjFyJntA+2awNeC0E5BxnzGR7L0PQ9Nn+lVOpvHrW27ePI5bU79UqqlHnnddwy23W72f7LRz6YEkMe100IHiWOb3o/bb2WLqPR+NV5nFp/yj9f75mRaarBr1Je5luztfGO9bsnx01ZaPoYytA+jSzyq/wDz/ZtVqMv4j3ceXOq7tHb2w5/vpNUmn1DnaWfUFZ1r0UUn63FL4L895h19ajBc5JfFi2zh6R0wra+Y1VVtp1HMcWOmPPHhsAPAeK7TT9IpWsVhLl1Lbx733nL32qzr5jHkn5v7Il8U2f42n5IcGPa8SMcc6dQBGDjww4rNu7f09Phzz3MSyuP09Tixy2M6zg+sLBHJcHBgAaIwZnsa0dGgFwGFqY6HHPE+HPgbd6ytlF+YsXZ/CPnqJHeelrWfnlZUdKh1yf55lp6rN7RX55E2Hguib1ZJJ6vkI/7cK9HTqC3Tfv8Atgod/XfWl7v9J0NjpGfLTRbdC5gefq7KvRtqMdooodxVlvJk3AGwGAOgGwCvFKEKFSGoVFHfh3SsK52MmjuUvDx+2HuuR1Jcmbq3PbbCfsx7Lhrn2jbQ2J1b8hVinuVM8t4ppXOkOAuq0+uoRNfWhk5WSwPeRkLIutUwsJlFO2NvQ8PNDdwueq30pPczY0kkVd94fABLQs2y1Bxe5aq0E0ZHeJ2Cu50++40jSXFDBYCqW9VQ1/ATVfLYIBsgyCFD2CMXOTBVh/hqXL6tQckzc2dQ9islY2WFpBzsvM7qk6dR5OmozUolNxJYTMdbPmW00vVHbMxLu19IZ2j4QlfKHSdAVtr3XVUjhGLQseFnodBTCFgaNsBcjVqOpLJuIQUUZXjS5asRAro9Bs3OopYNXf1lGOCtoY9LAvUaMOGKRylSWWSVdLYoUlLHAoUNDwULbRTXrhmCskEr3SMcGhp0FveA6ZyDusSvZU60uJ5TMijdzox4VjAUfCFFHgmIyEeMr3Oz7gYB+iQsKEerPiU1L+vLrx4F9BG1jQxjWsaPla0BrR7ALMjFRWEsIwJ5k8t5Z1DlJRgNuuB7oRgXUhGBMoTgQlCpIYShWkNJUFaQwlC4kMJUFxIYShWkIoKhChUUl9PdKw7l8jIo7lHYGnnD3XI6k1hm6tz22wfox7Lhbn2jbQ2LOVuRhY8XgrKeos7XuyQsuNw4rBbcMk2joGsGwVmpVcipRwTNgrO5UVN3rGBpzhZdClJvkUTksHmd5kDpO75rttKpTWDUXUkMaw4HsutSeDUNou1nmKCAEBS362c1uodQsK6t1URkUavCzhw3xDJSO5cmdK4jU9IcstI31td4PRaDiCGUA6guSrWNSm9jbwuIyRONdEBnUFY9BUfUXPSRKS88SMY0tYcuWzsdKqVZLKMSvdxijKwRuleZH/cvStL05UII5i7uXUZZBbswBUIFQgUKSlocChS0OBQoaHgqShocHIUOIoKkp4RdSEcIupBwiFyE8I0uUEqI0lCtIaShWkNJUFaQ0lCtIaVBUNJwmScEOprA1WKlVRRdjTbKicOmOAtHe38UjY0Ldl3w9w+QQ4hcbf33Fk3NChg9EoG6GgLm6k+JmwjDBOa9Wg0OQpOcswaNyq4xbIbM9d781gIBWxtrKU2WJ1UjE3K7PlJAJXVWOlbZRra90R6alJOSustrNQRqatdyLEQBbDgRi8R3VwpBACAQhAQay1sk8N1YqUIz3LkKriV39jPYe44ha6rpVOfUZcLySJMdJN0Lz9VZjolJPYqd/IkQ28A5cclbGjZU6WyMWpcSkTmtA2CzEsFgVSAQAhAqEC5UkYHAoUtCgoUNDgUKcC5UkYFyhHCGpBwiakHCIShVgQlQVJDSUKkhpKFWBCoKjnJKGqlywVJZKurrvALBr3SgjJp0WznS0T5j44XNX2qJbM2tC1NbaLCG4JC5G71CU3ubejbpGkgp2sGwWonUcjNjBI7BWyseHqCGglqNIyrkFllqawY+/wB+Iy0Fb+xsPSYNfWrcJlHyvmOd12VlpiitjT1rkmUtFjcroKVBRRrp1Gyc1oCyUsFnI5SAQAgBACAEAIAQAgBACAEAIAQgVCBcoRgMqSMC5QjAuUIwLlCMBlBgTKDAZQnAmUKsCZQnAigkZI7AUNlSRnbtccHC1tzX4UZlGnk7WCn5zgSuR1G9ksm4t6CPRLZa2sA2XIXFzKTNxTpJFq1oCwW8mQlgZLMG9SqowbIckjjHXNJxlXXRaRb9ISQcqw1gupka4nuH2V6h7RbqbHmt3yZT7rv9Hgmkc/eMmUMIDV2dKKSNHOXMlq8WxUAIAQAgBACAEAIAQAgBACAEAIAQAhAIBUIDKDAuVJGAygwGUGAygwJlCcAoAiEggOcwyFTLYqRj77Tuzlai6ptmfQkh3Dt15LgCuWvrVyNtRq4PUbRemSNG65S4tZRZtadVMm1VyY0ZyrFO2lJlcqqSMZf+JsZAK3drpz3aMGrcHHhy7OleN1VeW6hEilPLPRKY5aFzdTc2kNjncB3CqqPtFNTY83u4+1Puu/0V8kc9eom0XyrtqexoZ7khXCkEAIAQAgBACAEAIAQAgBACAEAIAQAgBACAEIBAKgBACARACEggBAIgK+4UzXA5WPVgmi7CTRkLhTBjsgrT3FGJsKVRkm1XORhwCtDcWsGzPhVaLmS5SPG5S2saeSKleRnrrk75W3/TxhHkYiqNsueDD3wud1NcmbG3PW6P5AuOq+0bmGwlb8hSj7QqbHnF6/Sn3Xe6K9jn70k0PyruKWxoJ7kpXSgEAID/2Q==""".replace("\n", "").replace("\r", "")
decode_image=base64.b64decode(encode_image)
image = Image.open(io.BytesIO(decode_image))
def start():
    global p,la,p1,p2,sym,op
    sym=op[q.get()]
    p=random.choice((p1.get(),p2.get()))
    if p==p1.get():la.config(text=str(p)+" Turn   {"+sym[0]+"}")
    if p==p2.get():la.config(text=str(p)+" Turn   {"+sym[1]+"}")
    la.grid(row=0,column=0,pady=50)
    c.tkraise()
    
def next(ro,co):
    global buttons,p1,p2,p,la,space,sym
    if buttons[ro][co]["text"]=="" and not(win()):
        if p==p1.get():
            p=p2.get()
            buttons[ro][co]["text"]=sym[0]
            if win():
                la.config(text=p1.get()+" won   {"+sym[0]+"}")
            else:
                la.config(text=p+" turn   {"+sym[1]+"}")
        elif p==p2.get():
            p=p1.get()
            buttons[ro][co]["text"]=sym[1]
            if win():
                la.config(text=p2.get()+" won    {"+sym[1]+"}")
            else:
                la.config(text=p+" turn   {"+sym[0]+"}")
            
        space()
def win():
    for ro in range(3):
        if buttons[ro][0]["text"]==buttons[ro][1]["text"]==buttons[ro][2]["text"] !="" :
            buttons[ro][0]["bg"]="green"
            buttons[ro][1]["bg"]="green"
            buttons[ro][2]["bg"]="green"
            return True
    for co in range(3):
        if buttons[0][co]["text"]==buttons[1][co]["text"]==buttons[2][co]["text"] !="" :
            buttons[0][co]["bg"]="green"
            buttons[1][co]["bg"]="green"
            buttons[2][co]["bg"]="green"
            return True
    if buttons[0][0]["text"]==buttons[1][1]["text"]==buttons[2][2]["text"] !="":
        buttons[0][0]["bg"]="green"
        buttons[1][1]["bg"]="green"
        buttons[2][2]["bg"]="green"
        return True
    if buttons[0][2]["text"]==buttons[1][1]["text"]==buttons[2][0]["text"] !="":
        buttons[0][2]["bg"]="green"
        buttons[1][1]["bg"]="green"
        buttons[2][0]["bg"]="green"
        return True
    return False
def space():
    global sp
    sp-=1
    if sp==0:
        if not(win()):
            la.config(text="Tie")
            for ro in range(3):
                for co in range(3):
                    buttons[ro][co]["bg"]="orange"
def ne(*ar):
    global p1
    if e2.get()=="":e2.focus()
    elif e1.get()=="":e1.focus()
    else:
        b.tkraise()
        global p
        ma.title("game starts")
        p1.set(e1.get())
        p2.set(e2.get())
        e1.unbind("<Return>")
def frame1():
    global a,e2,e1
    a=Frame(ma)
    ma.title("Login")
    Label(a,text="Player 1 Name:",font=("consolas",20)).grid(row=0,column=0,padx=20)
    Label(a,text="Player 2 Name:",font=("consolas",20)).grid(row=2,column=0,padx=20)
    e1=Entry(a,font=("consolas",20))
    e1.grid(row=1,column=0,padx=100)
    e2=Entry(a,font=("consolas",20))
    e2.grid(row=3,column=0,padx=100)
    e1.bind("<Return>",ne)
    Button(a,text="Login",command=ne,font=("consolas",20)).grid(row=4,column=0,columnspan=2)
    Button(a,text="Exit",command=lambda: ma.destroy(),font=("consolas",20)).grid(row=5,column=0,columnspan=2)
    Label(a,text="WELCOME TO\nTHE GAME\nTIC TAK TAO",font=("consolas",50),fg="#186a99").grid(row=6,column=0,pady=100)
def frame2():
    global b,p1,p2,p
    b=Frame(ma)
    Label(b,text="Player Info:",font=("consolas",20)).grid(row=0,column=0)
    Label(b,textvariable=p1,font=("consolas",20)).grid(row=1,column=0)
    Label(b,textvariable=p2,font=("consolas",20)).grid(row=2,column=0)
    b1=Frame(b)
    Button(b1,text="continue",command=lambda:d.tkraise(),font=("consolas",20)).grid(row=0,column=0)
    Button(b1,text="Edit",command=lambda:a.tkraise(),font=("consolas",20)).grid(row=0,column=1)
    b1.grid(row=3,column=0)
    Button(b,text="Exit",command=lambda: ma.destroy(),font=("consolas",20)).grid(row=4,column=0,columnspan=2)
    Label(b,text="HERE WE GO\nCONFORM YOUR\nNAMES PLEASE",font=("consolas",50),fg="sky blue",bg="light yellow").grid(row=5,column=0,pady=100,padx=20)
def frame3():
    global d,q,sym,op
    d=Frame(ma)
    q=IntVar()
    q.set(0)
    op=[["X","O"],["@","#"],["$","%"],["*","&"]]
    for x in range(len(op)):
        ra=Radiobutton(d,text=str(op[x]),variable=q,value=x,font=("consolas",63),bg="gray",indicatoron=0)
        ra.pack(anchor=W,padx=20)
    Button(d,text="start",command=start,font=("consolas",50),fg="light green").pack(pady=100)
    
def frame4():
    global c,p1,p2,p,la
    c=Frame(ma)
    def re():
        global sp
        sp=9
        for ro in range(3):
            for col in range(3):
                buttons[ro][col]=Button(c2,text="",width=10,height=5,font=("consolas",20),command=lambda ro=ro,col=col:next(ro,col))
                buttons[ro][col].grid(row=ro,column=col)
        start()
        c.tkraise()
    def res():
        global p1,p2,sp
        sp=9
        re()
        a.tkraise()
    c3=Frame(c)
    Button(c3,text="Restart",font=("consolas",20),command=re).grid(row=0,column=0)
    Button(c3,text="Reset",font=("consolas",20),command=res).grid(row=0,column=1)
    Button(c3,text="Exit",command=lambda: ma.destroy(),font=("consolas",20)).grid(row=1,column=0,columnspan=2)
    c3.grid(row=2,column=0)
    c2=Frame(c,padx=15)
    c2.grid(row=1,column=0)
    for ro in range(3):
        for col in range(3):
            buttons[ro][col]=Button(c2,text="",width=10,height=5,font=("consolas",20),command=lambda ro=ro,col=col:next(ro,col))
            buttons[ro][col].grid(row=ro,column=col)
ma=Tk()
ma.resizable(False,False)
img=ImageTk.PhotoImage(image)
ma.iconphoto(True,img)
sp=9
buttons=[[0,0,0],[0,0,0],[0,0,0]]
p1=StringVar()
p1.set("")
p2=StringVar()
p2.set("")
frame1()
frame2()
frame3()
frame4()
for i in a,b,c,d:
    i.grid(row=0,column=0,sticky=NSEW)
a.tkraise()
la=Label(c,font=("consolas",20))
ma.mainloop()