#!/usr/bin/env bash
# Локальный просмотр Allure: нужен Java 17+ и Allure CLI.
# Варианты CLI:
#   macOS: brew install allure
#   или без установки (нужны Node.js + Java): этот скрипт попробует npx.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ ! -d allure-results ]] || [[ -z "$(find allure-results -mindepth 1 -print -quit 2>/dev/null)" ]]; then
  echo "Нет данных в allure-results. Сначала: pytest tests/"
  exit 1
fi

if command -v allure >/dev/null 2>&1; then
  exec allure serve allure-results
fi

if command -v npx >/dev/null 2>&1; then
  echo "Allure CLI не в PATH — запуск через npx (нужны Node.js и Java)…"
  exec npx --yes --package=allure-commandline@2.30.0 allure serve allure-results
fi

echo "Не найден ни allure, ни npx."
echo "Установите один из вариантов:"
echo "  brew install allure          # macOS / Linuxbrew"
echo "  или: https://github.com/allure-framework/allure2/releases"
echo "Проверьте: java -version   (нужна JRE 8+)"
exit 1
