#!/bin/bash

# Configuración
APP_NAME="tabata-app"
INSTALL_DIR="/opt/$APP_NAME"
BIN_DIR="/usr/bin"
ICON_DIR="/usr/share/icons/hicolor/scalable/apps"
DESKTOP_DIR="/usr/share/applications"

echo "🚀 Instalando $APP_NAME..."

# 1. Build dir and copy files
sudo mkdir -p $INSTALL_DIR
sudo cp -r ./* $INSTALL_DIR

# 2. build symbolic link to app
# Assure yout app has permissions chmod +x app.py
sudo ln -sf $INSTALL_DIR/main.py $BIN_DIR/$APP_NAME

# 3. Install icon
sudo mkdir -p $ICON_DIR
sudo cp assets/icon.svg $ICON_DIR/tabata-icon.svg

# 4. install launch menu
sudo cp $APP_NAME.desktop $DESKTOP_DIR/

# 5. update desktop database
sudo update-desktop-database

echo "✅ Ready! Search '$APP_NAME' in your menu."