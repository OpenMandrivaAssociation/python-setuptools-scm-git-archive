# Created by pyp2rpm-3.3.1
%global pypi_name setuptools-scm-git-archive

Name:           python-%{pypi_name}
Version:        1.0
Release:        %mkrel 4
Summary:        setuptools_scm plugin for git archives
Group:          Development/Python
License:        MIT
URL:            https://github.com/Changaco/setuptools_scm_git_archive/
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/setuptools_scm_git_archive-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)

%description
This is a setuptools_scm plugin that adds support for git archives (for
example the ones GitHub automatically generates). Note that it only works for
archives of tagged commits (because git currently lacks a format option
equivalent to git describe --tags).

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)

%description -n python3-%{pypi_name}
This is a setuptools_scm plugin that adds support for git archives (for
example the ones GitHub automatically generates). Note that it only works for
archives of tagged commits (because git currently lacks a format option
equivalent to git describe --tags).

%prep
%autosetup -n setuptools_scm_git_archive-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/setuptools_scm_git_archive/
%{python3_sitelib}/setuptools_scm_git_archive-*-py?.?.egg-info/
