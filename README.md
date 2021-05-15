[![Issues](https://img.shields.io/github/issues/jainamoswal/PyTgAuth?style=for-the-badge&color=green)](https://github.com/jainamoswal/PyTgAuth/issues)
[![Stars](https://img.shields.io/github/stars/jainamoswal/PyTgAuth?style=for-the-badge&color=green)](https://github.com/jainamoswal/PyTgAuth)
[![Size](https://img.shields.io/github/repo-size/jainamoswal/PyTgAuth?style=for-the-badge&color=green)](https://github.com/jainamoswal/PyTgAuth)

---
## Support 
- [![Channel](https://img.shields.io/badge/Telegram-Channel-green?style=for-the-badge&logo=telegram)](https://t.me/J_projects)
- [![Support](https://img.shields.io/badge/Telegram-Group-green?style=for-the-badge&logo=telegram)](https://t.me/J_projects_chat)

---

## Verify [Telegram Auth](https://core.telegram.org/widgets/login#checking-authorization) via website or Bot.

<details><summary><b>Installation.</b></summary>
<p><br>
</a>
<code>pip install pytgauth --upgrade</code>
</p>
</details>

<details><summary><b>Sample data from Telegram.</b></summary>
<p>

```
{
    "id": XXXXXXXXX,
    "first_name": "XXX",
    "last_name": "XXX",
    "username": "XXXXX",
    "photo_url": "https://t.meXXXXXX.jpg",
    "auth_date": XXXXXXXXXX,
    "hash": "XXXXXXXXXXXXXXXXXXXXXX....."
}
```

---

</p>
</details>

```
from pytgauth import verify
bot_token = 'xxx:xxxx'
data = {...}

if verify(data, bot_token):
    print('Hey ! You are verified.')
else:
    print('Upps, the data is not verified')
```

[Watch the Example.py for more information.](https://github.com/jainamoswal/PyTgAuth/blob/main/example.py)


## License 
### [PyTgAuth](https://github.com/jainamoswal/PyTgAuth) is licensed under [GNU Affero General Public License v3](https://www.gnu.org/) or later.

[![License](https://www.gnu.org/graphics/gplv3-or-later.png)](LICENSE)

`The GNU General Public License (GNU GPL or simply GPL) is a series of widely-used free software licenses that guarantee end users the freedom to run, study, share, and modify the software.[8] The licenses were originally written by Richard Stallman, founder of the Free Software Foundation (FSF), for the GNU Project, and grant the recipients of a computer program the rights of the Free Software Definition.[9] The GPL series are all copyleft licenses, which means that any derivative work must be distributed under the same or equivalent license terms. This is in distinction to permissive software licenses, of which the BSD licenses and the MIT License are widely used, less restrictive examples. GPL was the first copyleft license for general use.`
