Name: python-dev-contain
Version: 5.0.3
Release: 1%{?dist}
Summary: Development container wrapper around podman

License: Apache-2.0
URL: https://github.com/jpace121/dev_contain
Source0: dev_contain

BuildArch: noarch

%global _description %{expand:
CLI script to build and use containers for development leveraging podman.}

%description %_description

%package -n python3-dev-contain
Summary: Facilitate development container use
BuildRequires: python3-devel
Requires: python3-jinja2 python3-pyyaml

%description -n python3-dev-contain %_description

%prep
cp -rf ${RPM_SOURCE_DIR}/dev_contain/* ${RPM_BUILD_DIR}

%build
%py3_build

%install
%py3_install


%files -n python3-dev-contain
%license LICENSE
%doc README.md
%{python3_sitelib}/dev_contain-*.egg-info/
%{python3_sitelib}/dev_contain/
%{_bindir}/dev_contain



%changelog
* Sat Jun 20 2020 James Pace <jpace121@gmail.com>
- Initial package.
