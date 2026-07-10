%global tl_name esieecv
%global tl_revision 59638

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Curriculum vitae for French use
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ESIEEcv
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esieecv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esieecv.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esieecv.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the user to set up a curriculum vitae as a French
employer will expect.

