[Setup] 
AppName=NPCS 
AppVersion=6.1 
WizardStyle=modern 

; --- FORCE LOCAL USER FOLDER --- 
DefaultDirName={localappdata}\Programs\NPCS 
DefaultGroupName=NPCS 
UninstallDisplayIcon={app}\NPCS.exe 
Compression=lzma2 
SolidCompression=yes 

; --- RELATIVE OUTPUT & ICON PATHS ---
; OutputDir=. creates NPCS_Setup.exe directly inside your NPCS_Bundle folder
OutputDir=.
OutputBaseFilename=NPCS_Setup 
SetupIconFile=NPCS_logotype.ico 

; --- RUN WITHOUT ADMIN PRIVILEGES --- 
PrivilegesRequired=lowest 

[Tasks] 
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked 

[Files] 
; Uses relative path to locate PyInstaller's dist folder
Source: "dist\NPCS\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs 

[Icons] 
Name: "{group}\NPCS"; Filename: "{app}\NPCS.exe"; IconFilename: "{app}\NPCS.exe" 
Name: "{autodesktop}\NPCS"; Filename: "{app}\NPCS.exe"; IconFilename: "{app}\NPCS.exe"; Tasks: desktopicon 

[Run] 
Filename: "{app}\NPCS.exe"; Description: "{cm:LaunchProgram,NPCS}"; Flags: nowait postinstall skipifsilent 

; --- SPREADSHEET SAVE LOCATION PROMPT ---
[Code]
var
  DataDirPage: TInputDirWizardPage;

procedure InitializeWizard;
begin
  // Adds a page to the installer asking where CSV spreadsheets should be saved
  DataDirPage := CreateInputDirPage(
    wpSelectDir,
    'Select Spreadsheet Save Directory', 
    'Where should NPCS save your inventory spreadsheets?',
    'Select the folder where NPCS will save your CSV files, then click Next.',
    False, 
    ''
  );
  DataDirPage.Add('');
  // Sets default to C:\Users\<User>\Documents\NPCS
  DataDirPage.Values[0] := ExpandConstant('{userdocs}\NPCS');
end;

procedure CurStepChanged(CurStep: TSetupStep);
var
  ConfigFile: String;
begin
  // Generates config.ini inside the app folder after installation finishes
  if CurStep = ssPostInstall then
  begin
    ConfigFile := ExpandConstant('{app}\config.ini');
    SetIniString('Settings', 'SaveDirectory', DataDirPage.Values[0], ConfigFile);
  end;
end;