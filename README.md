# Project Market ChoKurly ๐ซ๐ช๐ฉ๐ญ๐ง
## ๐ฅ Project Summary
- 2021.04.12 ~ 2021.04.23 ๊น์ง 2์ฃผ ๊ฐ ์งํ
- ๊ตญ๋ด ์ํ ์ ๋ฌธ ์จ๋ผ์ธ ์ผํ๋ชฐ์ธ ๋ง์ผ ์ปฌ๋ฆฌ๋ฅผ ํด๋ก ํ๋ ํ๋ก์ ํธ
- Front(์ด์์, ์๋์ด, ์ฑ์คํ)์ Back(๋ฐฑ์น์ฐฌ, ์์ ํ, ๊น์ํ) ์ด 6๋ช์ ํ์์ผ๋ก ๊ตฌ์ฑ

## ๐ฉ๐ปโ๐ป Front-end Work Details
### ์ด์์
- `Nav`: ๊ณตํต์ผ๋ก ์ฐ์ด๋ Nav ์ปดํฌ๋ํธ
    - ์คํฌ๋กค ์ Nav ๋ฐ๊ฐ ๊ฐ๋ ค์ง๋ ์์ ๋ถํฐ ๊ณ ์  ๊ธฐ๋ฅ
    - ์ ์ฒด ์นดํ๊ณ ๋ฆฌ์ ๋ง์ฐ์ค ์ค๋ฒ ์ ์๋ฒ๋ก๋ถํฐ ๋ฐ์์จ ์นดํ๊ณ ๋ฆฌ ๋ฆฌ์คํธ ๋๋กญ๋ค์ด
    - ์ ์ฒด ์นดํ๊ณ ๋ฆฌ๊ฐ ์ ํ ๋์์ ์์๋ง ์๋ธ ์นดํ๊ณ ๋ฆฌ ์กฐ๊ฑด๋ถ ๋ ๋๋ง
- `Main`: ์น ์ฑ์ ์ฒซ ๋ฉ์ธ ํ์ด์ง
    - ์๋์ผ๋ก ์ฌ๋ผ์ด๋ ๋๋ ์บ๋ฌ์, ์บ๋ฌ์ ํํฐ๋ง ๊ธฐ๋ฅ
    - 24์๊ฐ ํ์  ์ธ์ผ์ ์ํ ํ์ด๋จธ ๊ธฐ๋ฅ
    - ์ด 6๊ฐ ์ถ์ฒ ํ๋ชฉ (suggestions, sales, new ๋ฑ) ์ผ๋ก ๋๋์ด์ง ์ํ๋ค์ ๊ฐ ์บ๋ฌ์๋ก ๊ตฌํ  
- `Product List`: ์ ํ๋ ์นดํ๊ณ ๋ฆฌ์ ์ํ ๋ฆฌ์คํธ ํ์ด์ง
    - ๋์  ๋ผ์ฐํ์ผ๋ก ๊ฐ ์๋ธ ์นดํ๊ณ ๋ฆฌ์ ์ํ ๋ฆฌ์คํธ ๊ตฌํ
    - ๋์  ๋ผ์ฐํ์ผ๋ก ์ ์ํ์, ๊ฐ๊ฒฉ์ ํํฐ๋ง ๊ตฌํ
    - Pagination ๊ตฌํ
    - ์ฅ๋ฐ๊ตฌ๋ ๋ชจ๋ฌ์ฐฝ ๊ธฐ๋ฅ ๊ตฌํ
### ์๋์ด
- `Footer`: ๋งจ ์๋ ๊ณ ์ . ํด๋น ํ์ด์ง๋ก ์ด๋ ๋งํฌ.
- `Product Details`: 
   - ์์ธํ์ด์ง๋ฅผ Thumbnail, related-product, product-description, review ๋ถ๋ถ์ผ๋ก ๋๋์ด ์ปดํฌ๋ํธํ ํ ๊ด๋ฆฌ. (state์ props๋ฅผ ์ฌ์ฉ)
   - ๊ด๋ จ์ํ: ๋ฒํผ ํด๋ฆญ์ ์ด๋ฏธ์ง ์ฌ๋ผ์ด๋ฉ(์บ๋ฌ์) ๊ธฐ๋ฅ ๊ตฌํ
   - ์๋๋ณ๊ฒฝ๋ฒํผ๊ณผ ์ํ์๋์ ๋ฐ๋ฅธ ๊ฐ๊ฒฉ๋ณ๋ ๊ตฌํ.
   - ๊ณ ๊ฐํ๊ธฐ&์ํ๋ฌธ์: ๋๊ธ ๊ธฐ๋ฅ๊ตฌํ
   - scrollTo()๊ตฌํ: ์์ธ์ ๋ณด/๋๊ธ ํญ ํด๋ฆญ์ ํด๋น์์น๋ก ์ด๋, ๋งจ์๋ก ์ด๋ ๋ฒํผ
   - ์ฅ๋ฐ๊ตฌ๋ ๋ด๊ธฐ: fetch() post๋ฅผ ์ด์ฉํด ์ฅ๋ฐ๊ตฌ๋ ํ์ด์ง๋ก ๋ฐ์ดํฐ ์ ๋ฌ.
- `Cart`:
   - ๋ ์ด์์
   - ์๋๋ณ๊ฒฝ ๋ฒํผ
   - ์ ์ฒด์ญ์  ๊ธฐ๋ฅ


### ์ฑ์คํ
- `Signup`:
   - Signup ํ์ด์ง ์ ๋ฐ์ ์ธ ๋ ์ด์์(html & CSS)
   - Id, Email ์ค๋ณต๊ฒ์ฌ ๋ฐฑ์๋์์ ์ํต
   - Id, Pw , Email ๋ฑ Validation ๊ธฐ๋ฅ
   - ํ์ํญ๋ชฉ, ์ ํํญ๋ชฉ ๊ตฌ๋ถ ํ, Login Information BackEnd๋ก ์ ๋ฌ
   - Sign up Fin Page ๊ตฌ์ฑ 
- `Login`: 
   - Login ํ์ด์ง ์ ๋ฐ์ ์ธ ๋ ์ด์์(html & CSS)
   - Login Info ์ ๋น๊ตํ Login ์งํ ๊ธฐ๋ฅ
   - Id ์ฐพ๊ธฐ ํ์ด์ง ๊ตฌ์ฑ ๋ฐ id์ฐพ๊ธฐ ๊ธฐ๋ฅ
   - Pw ์ฐพ๊ธฐ ํ์ด์ง ๊ตฌ์ฑ ๋ฐ pw์ฐพ๊ธฐ ๊ธฐ๋ฅ ( ์ด๋ฉ์ผ๋ก ๋ฐ๊ธ๋ ์์๋น๋ฐ๋ฒํธ๋ก ๋ก๊ทธ์ธ ๊ฐ๋ฅ)
- `Cart`:
   - ์ฅ๋ฐ๊ตฌ๋ ํ์ด์ง ๊ตฌ์ฑ
   - ํน์  ํ์์ ์ฅ๋ฐ๊ตฌ๋์ ๊ฐ๋ณ ์ํ๋ง๋ค ์๋ ์ฆ๊ฐ ๋ฒํผ ๊ธฐ๋ฅ
   - ํน์  ํ์์ ์ฅ๋ฐ๊ตฌ๋์ ์ ์ฒด ์ญ์  ๋ฒํผ ๊ธฐ๋ฅ
   - ํน์  ํ์์ ์ฅ๋ฐ๊ตฌ๋์ ๊ฐ๋ณ ์ญ์  ๋ฒํผ ๊ธฐ๋ฅ
   - ์ ํํ ์ํ๋ค ๊ณ์ฐ๊ฒฐ๊ณผ ํ์ (ํ ์ธ๊ฐ ์ ์ฉ ๊ฐ๋ฅ)
   - ํน์  ์กฐ๊ฑด(~์ ์ด์์)๋ฌ์ฑ ์ ๋ฌด๋ฃ๋ฐฐ์ก ์กฐ๊ฑด ๊ตฌํ

## ๐ฉ๐ปโ๐ป Back-end Work Details
### ๋ฐฑ์น์ฐฌ
- 'users'
    - FindIdView ๊ธฐ๋ฅ ๊ตฌํ
    - FindPasswordView ๊ธฐ๋ฅ ๊ตฌํ
    - ReviewView ๊ธฐ๋ฅ ๊ตฌํ
    - UserLikeView ๊ธฐ๋ฅ ๊ตฌํ
- 'products'
    - CategoryView ๊ธฐ๋ฅ ๊ตฌํ
    - ProductListView ๊ธฐ๋ฅ ๊ตฌํ
    - SearchView ๊ธฐ๋ฅ ๊ตฌํ
### ์์ ํ
- `User`
    - UserView ๊ธฐ๋ฅ๊ตฌํ
    - LoginView ๊ธฐ๋ฅ๊ตฌํ
    - SignupCheckView ๊ธฐ๋ฅ ๊ตฌํ
- `Order`
    - OrderformView  ๊ธฐ๋ฅ ๊ตฌํ
    - OrderDetailView ๊ธฐ๋ฅ ๊ตฌํ
### ๊น์ํ
- `Decorator`
    - login_required ๊ธฐ๋ฅ ๊ตฌํ
- `Product_detail`
    - ProductDetail View ๊ธฐ๋ฅ ๊ตฌํ
- `Basket` 
    - ์ฅ๋ฐ๊ตฌ๋ View ๊ธฐ๋ฅ ๊ตฌํ
    - Cart ๊ธฐ๋ฅ ๊ตฌํ
    - ์ฅ๋ฐ๊ตฌ๋ ์๋ ์กฐ์  ๊ธฐ๋ฅ View ๊ตฌํ
## ๐ง Skills
- ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
- ![SASS](https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white)
- ![JS](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
- ![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
- ![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
- ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

## ๐ง Tools
- <img alt="Trello" src="https://img.shields.io/badge/Trello-%23026AA7.svg?&style=for-the-badge&logo=Trello&logoColor=white"/>
- <img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?&style=for-the-badge&logo=git&logoColor=white"/>
- <img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/>
- <img alt="Slack" src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white" />
- <img alt="AWS" src="https://img.shields.io/badge/AWS-%23FF9900.svg?&style=for-the-badge&logo=amazon-aws&logoColor=white"/>
- <img alt="Visual Studio Code" src="https://img.shields.io/badge/VisualStudioCode-0078d7.svg?&style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
## โ๏ธ Blogs
- ์ด์์ : https://jessywlee.medium.com
- ์๋์ด : https://velog.io/@seod0209/Project-2.-%EB%A7%88%EC%BC%93%EC%BB%AC%EB%A6%AC-%ED%81%B4%EB%A1%A0
- ์ฑ์คํ : https://velog.io/@hello1358
- ๋ฐฑ์น์ฐฌ : https://velog.io/@chan_baek
- ์์ ํ : https://velog.io/@tgrf07
- ๊น์ํ : https://velog.io/@fcfargo

## โ๏ธ References
- ์ด ํ๋ก์ ํธ๋ ๋ง์ผ ์ปฌ๋ฆฌ๋ฅผ ์ฐธ๊ณ ํ์ฌ ํ์ต์ฉ์ผ๋ก ์์ ๋์์ต๋๋ค.
- ์ด ํ๋ก์ ํธ์์ ์ฌ์ฉ๋ ๋ชจ๋  ๋ฌด๋ฃ ์ด๋ฏธ์ง๋ Unsplash์์ ๊ฐ์ ธ์์ต๋๋ค.
