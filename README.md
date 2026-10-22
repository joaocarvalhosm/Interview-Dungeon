# Interview Dungeon

A dungeon crawler for tech interview prep, inspired by Diablo 1.

You create a hero, pick one or more dungeons (each one is a real job target, like
**Google SWE Intern**), and go down floor by floor. Every floor is a skill the real
interview tests, and every floor ends in a boss that copies the real interview
format. Clearing a floor is your proof that you know that skill, as of that date.

> **Status:** design stage. The first path (Google SWE Intern) is fully designed and
> there is a clickable prototype with sample data. No app code yet.
> See the [roadmap](docs/roadmap.md).

**Website: https://renilsonjr.github.io/Interview-Dungeon/**

## Why this exists

Most people prepare for tech interviews blind:

- They grind problems without knowing what their target company actually tests.
- They have no honest way to know if they're ready.
- They quit halfway, because there's no visible finish line.

Interview Dungeon tries to fix that with three ideas:

1. **Readiness per company, with sources.** Every requirement in a path is labeled
   *Official* (the company says it), *Reported* (candidates say it, consistently)
   or *Estimated* (our own judgment). The app never presents a guess as a fact.
2. **Bosses copy the real format, not only the topic.** A Google boss is an unseen
   medium problem in a plain editor, with no running code and 45 minutes on the clock.
3. **One shared skill tree.** You study arrays once, and it counts for every dungeon
   that tests arrays.

It's also a **dev diary**: every hero has a scroll for general notes, plus notes for
each zone and each floor.

## Play the demo

**Play it online: https://renilsonjr.github.io/Interview-Dungeon/prototype/**

The demo is Floor III (Arrays) of the Google SWE Intern path, shortened:

- Create a hero (the class only changes how it looks).
- **Learn** three array patterns, in English or Brazilian Portuguese.
- **Recognize:** a quiz where wrong answers come back at the end.
- **Four coding problems.** Real Python runs in your browser, with sample tests and hidden tests.
- **The boss:** 45 minutes, no running code, approach before coding, then state the complexity.
- **The dev scroll:** your notes, general and per floor.

Your progress is saved in your own browser only. Nothing is sent anywhere.

## How a dungeon works

| Piece | What it is |
|---|---|
| **Zone** | A group of floors (4 per dungeon) |
| **Floor** | One skill, like Arrays or Team match |
| **Run** | The steps inside a floor: learn, quiz, easy and medium problems, explain |
| **Boss** | Closes a floor. Copies the real interview format |
| **Final boss** | The full interview loop. Confirms the path |

The full design is in [`docs/design.md`](docs/design.md), and the first path is in
[`docs/paths/google-swe-intern.md`](docs/paths/google-swe-intern.md).

## How you can help

**Join the community on Discord: https://discord.gg/cfDFY9NZMj**

You don't need to write code to contribute. The most valuable help right now:

- **Share your interview experience.** If you've interviewed for a role, tell us how
  the process went: rounds, formats and topics. This is what turns *Reported* data into
  reliable paths. Use the **Interview report** issue template.
- **Propose a new dungeon.** Applying somewhere that isn't covered yet? Open a
  **New path** issue with what you know and your sources.
- **Play the prototype and give feedback.** What's confusing, what's missing, what
  would make you actually use it. Use the **Feedback** template.
- **Write or translate learning pages**, in English or Brazilian Portuguese.
- **Code**, once the stack is confirmed. Issues labeled `good first issue` will
  show up as the build starts.

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request, especially
the rules about interview NDAs and copied content.

## Rules this project follows

- **No copied problems.** Challenges are original, inspired by common patterns. Nothing
  is copied from LeetCode or any other platform.
- **No company secrets.** We describe interview *formats and topics*, never questions
  you agreed to keep confidential.
- **Inspired by Diablo, not using Diablo.** No Blizzard names, logos, art, fonts or
  characters.
- **Not affiliated** with Google, Ramp, Mercury or any company mentioned here.
  Company names only describe the role a path prepares for.

Details in [`docs/ip-rules.md`](docs/ip-rules.md).

## Em português

O Interview Dungeon é um jogo, inspirado no Diablo 1, para se preparar para entrevistas
de tecnologia. Cada masmorra é uma vaga real, cada andar é uma habilidade que a
entrevista cobra, e cada andar termina num chefe que copia o formato real da entrevista.

Entre no nosso Discord: https://discord.gg/cfDFY9NZMj

Se você chegou aqui por um dos vídeos: a forma mais útil de ajudar agora é **contar como
foi a sua entrevista** (etapas, formato e assuntos, sem revelar perguntas confidenciais),
usando o modelo de issue **Interview report**. Também dá para jogar o protótipo
(https://renilsonjr.github.io/Interview-Dungeon/prototype/) e dar a sua opinião, propor uma masmorra nova, ou escrever páginas de estudo em português.

## License

[MIT](LICENSE). By contributing, you agree that your contributions are licensed under
the same terms.
