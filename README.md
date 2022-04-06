<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/arbanhossain/everything-placeholder">
    <img src="logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Everything Placeholder</h3>

  <p align="center">
    Placeholders for anything and everything you need with zero local dependency.
    <br />
    <a href="#endpoints"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/arbanhossain/everything-placeholder/issues">Report Bug</a>
    ·
    <a href="https://github.com/arbanhossain/everything-placeholder/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    </li>
      <li><a href="#endpoints">Endpoints</a>
      <ul>
        <li><a href="#/images">/images</a>
        <li><a href="#/text">/text</a>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The project is aimed at assisting developers by giving them access to a wide variety of items to use as a placeholder so that they can worry about what matters the most - actually developing the software. As of April 2022, images and texts are available with a moderate amount of options for generating unique placeholders.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Flask](https://flask.palletsprojects.com/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

The resources are available via an API hosted at [https://arbanh.tech](https://arbanh.tech). For example, to generate an image of a desired width of 800px and a desired height of 600px, make a request to `https://arbanh.tech/images?width=800&height=600`. The following image is sent back as the response.

A complete list of available endpoints is featured [here](#endpoints).



<p align="right">(<a href="#top">back to top</a>)</p>

## Endpoints

- ### /images

| Parameters  | Description |
| ----------- | ----------- |
| width | Desired width of the image, in pixels |
| height | Desired height of the image, in pixels |
| color | Desired color of the image, as CSS3-style color specifiers. Additional information is available [here](https://pillow.readthedocs.io/en/stable/reference/ImageColor.html) |

- ### /text
| Parameters  | Description |
| ----------- | ----------- |
| paragraphs | Desired number of paragraphs in the text. If used with `words`, will be ignored |
| words | Desired number of words in the text. If used with `paragraphs`, this will take precedence. |

<!-- ROADMAP -->
## Roadmap

- [ ] Audio
- [ ] Video
- [ ] Code
    - [ ] Support multiple languages

See the [open issues](https://github.com/arbanhossain/everything-placeholder/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Any and every contribution under moderation is greatly appreciated. 

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.md` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Arban Hossain - [@arbanhossain](https://github.com/arbanhossain) - arbanhossain@gmail

Project Link: [https://github.com/arbanhossain/everything-placeholder/](https://github.com/arbanhossain/everything-placeholder/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/arbanhossain/everything-placeholder.svg?style=for-the-badge
[contributors-url]: https://github.com/arbanhossain/everything-placeholder/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/arbanhossain/everything-placeholder.svg?style=for-the-badge
[forks-url]: https://github.com/arbanhossain/everything-placeholder/network/members
[stars-shield]: https://img.shields.io/github/stars/arbanhossain/everything-placeholder.svg?style=for-the-badge
[stars-url]: https://github.com/arbanhossain/everything-placeholder/stargazers
[issues-shield]: https://img.shields.io/github/issues/arbanhossain/everything-placeholder.svg?style=for-the-badge
[issues-url]: https://github.com/arbanhossain/everything-placeholder/issues
[license-shield]: https://img.shields.io/github/license/arbanhossain/everything-placeholder.svg?style=for-the-badge
[license-url]: https://github.com/arbanhossain/everything-placeholder/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png